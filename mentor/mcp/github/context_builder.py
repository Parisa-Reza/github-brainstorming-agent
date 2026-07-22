import json


class GitHubContextBuilder:

    def build(
        self,
        tool,
        result,
    ):

        if result is None or result.isError:

            return ""

        if not result.content:
            return ""

        text = result.content[0].text

        if tool == "get_file_contents":

            return (
                "GITHUB MCP CONTEXT\n"
                "====================\n\n"
                + text
            )

        if tool == "list_branches":

            branches = json.loads(text)

            context = (
                "GITHUB MCP CONTEXT\n"
                "====================\n\n"
                "Repository Branches\n\n"
            )

            for branch in branches:

                context += f"- {branch['name']}\n"

            return context

        if tool == "list_commits":

            commits = json.loads(text)
            latest = commits[0]

            context = (
                "GITHUB MCP CONTEXT\n"
                "====================\n\n"
            )

            context += (
                "Latest Commit\n\n"
                f"Message: {latest['commit']['message']}\n"
                f"Author: {latest['commit']['author']['name']}\n"
                f"Date: {latest['commit']['author']['date']}\n\n"
            )

            context += "Recent Commit History\n\n"

            for commit in commits[:5]:

                context += (
                    f"Commit: {commit['commit']['message']}\n"
                    f"Author: {commit['commit']['author']['name']}\n"
                    f"Date: {commit['commit']['author']['date']}\n\n"
                )

            return context

        if tool == "get_commit":

            commit = json.loads(text)
            details = commit.get("commit", {})
            author = details.get("author", {})
            stats = commit.get("stats", {})

            context = (
                "GitHub Commit Details\n\n"
                f"SHA: {commit.get('sha', 'unknown')}\n"
                f"Message: {details.get('message', 'unknown')}\n"
                f"Author: {author.get('name', 'unknown')}\n"
                f"Date: {author.get('date', 'unknown')}\n"
                f"Files changed: {len(commit.get('files', []))}\n"
                f"Additions: {stats.get('additions', 0)}\n"
                f"Deletions: {stats.get('deletions', 0)}\n\n"
                "Changed files\n"
            )

            for file in commit.get("files", []):
                context += (
                    f"- {file.get('filename', 'unknown')} "
                    f"({file.get('status', 'modified')}, "
                    f"+{file.get('additions', 0)} / -{file.get('deletions', 0)})\n"
                )
                patch = file.get("patch")
                if patch:
                    context += f"```diff\n{patch}\n```\n"

            return context

        
        if tool == "list_pull_requests":

            pull_requests = json.loads(text)

            context = (
                "GITHUB MCP CONTEXT\n"
                "====================\n\n"
                "Pull Requests\n\n"
            )

            if not pull_requests:

                context += "No pull requests found."

                return context

            for pr in pull_requests:

                context += (
                    f"Title: {pr['title']}\n"
                    f"Author: {pr['user']['login']}\n"
                    f"State: {pr['state']}\n"
                    f"Number: #{pr['number']}\n\n"
                )

            return context

        return text
