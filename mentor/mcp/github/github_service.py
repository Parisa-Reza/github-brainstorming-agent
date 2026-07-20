import asyncio

from mentor.mcp.github.github_client import (
    GitHubMCPClient,
)

# from mentor.mcp.github.response_formatter import (
#     MCPResponseFormatter,
# )

from mentor.mcp.github.context_builder import (
    GitHubContextBuilder,
)


class GitHubService:

    def __init__(self):

        self.client = GitHubMCPClient()
        # self.formatter = MCPResponseFormatter()
        self.context_builder = GitHubContextBuilder()

    def get_file_contents(
        self,
        owner,
        repo,
        path,
    ):

        result = asyncio.run(

            self.client.call_tool(

                "get_file_contents",

                {
                    "owner": owner,
                    "repo": repo,
                    "path": path,
                },
            )
        )

        if result.isError:

            return None

        for item in result.content:

            if hasattr(item, "resource"):

                return item.resource.text

        return None

    def list_commits(
        self,
        owner,
        repo,
    ):

        return asyncio.run(

            self.client.call_tool(

                "list_commits",

                {
                    "owner": owner,
                    "repo": repo,
                },
            )
        )

    def search_code(
        self,
        query,
    ):

        return asyncio.run(

            self.client.call_tool(

                "search_code",

                {
                    "query": query,
                },
            )
        )

    def execute(
        self,
        route,
    ):

        if route is None:

            return None

        tool = route["tool"]

        args = route["args"]

        result = asyncio.run(

            self.client.call_tool(

                tool,

                args,
            )
        )

        if result.isError:

            return None
            
        return self.context_builder.build(

                tool,

                result,
            )