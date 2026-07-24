import asyncio
import json

from mentor.mcp.github.github_client import (
    GitHubMCPClient,
)

from mentor.mcp.github.context_builder import (
    GitHubContextBuilder,
)


class GitHubService:

    def __init__(self):

        self.client = GitHubMCPClient()
        # self.formatter = MCPResponseFormatter()
        self.context_builder = GitHubContextBuilder()

    async def get_file_contents(
        self,
        owner,
        repo,
        path,
    ):

        result = await self.client.call_tool(

            
                "get_file_contents",

                {
                    "owner": owner,
                    "repo": repo,
                    "path": path,
                },
            
        )

        if result.isError:

            return None

        for item in result.content:

            if hasattr(item, "resource"):

                return item.resource.text

        return None

    async def list_commits(
        self,
        owner,
        repo,
    ):

        return await self.client.call_tool(

        
                "list_commits",

                {
                    "owner": owner,
                    "repo": repo,
                },
            
        )

    async def search_code(
        self,
        query,
    ):

        return await self.client.call_tool(

            

                "search_code",

                {
                    "query": query,
                },
            
        )

    async def execute(
        self,
        route,
    ):

        if route is None:

            return None

        tool = route["tool"]

        args = route["args"]

        if tool == "get_commit_details":
            return await self.get_commit_details(
                owner=args["owner"],
                repo=args["repo"],
                question=args["question"],
            )

        result = await self.client.call_tool( tool, args )

  return None

        if result.isError:
            raise Exception(result)
            
        return self.context_builder.build(

                tool,

                result,
            )

    async def get_commit_details(
        self,
        owner: str,
        repo: str,
        question: str,
    ):
        """Find the requested commit, then ask GitHub for its changed files."""
        commits_result = await self.list_commits(owner, repo)

        if commits_result.isError or not commits_result.content:
            return "GitHub could not load the commit history."

        try:
            commits = json.loads(commits_result.content[0].text)
        except (IndexError, TypeError, json.JSONDecodeError):
            return "GitHub returned commit history in an unexpected format."

        commit = self._find_commit(commits, question)

        if not commit:
            return "I could not find that commit in the active repository's commit history."

        sha = commit.get("sha")
        if not sha:
            return "GitHub did not provide an identifier for the requested commit."

        result = await self.client.call_tool(
                "get_commit",
                {
                    "owner": owner,
                    "repo": repo,
                    "sha": sha,
                },
            
        )

        if result.isError:
            return "GitHub could not load the changed files for that commit."

        return self.context_builder.build("get_commit", result)

    @staticmethod
    def _find_commit(commits, question: str):
        question = question.lower()

        for commit in commits:
            message = commit.get("commit", {}).get("message", "")
            issue_key = (
                message.split("]", 1)[0] + "]"
                if message.startswith("[") and "]" in message
                else ""
            )

            if message.lower() in question or (issue_key and issue_key.lower() in question):
                return commit

        return None
