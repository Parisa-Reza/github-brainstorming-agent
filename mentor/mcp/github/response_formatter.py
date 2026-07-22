import json


class MCPResponseFormatter:

    def format(
        self,
        tool,
        result,
    ):

        if result.isError:

            return "GitHub MCP request failed."

        text = result.content[0].text

        if tool == "get_file_contents":

            return text

        if tool == "list_branches":

            branches = json.loads(text)

            output = "# Repository Branches\n\n"

            for branch in branches:

                output += f"- {branch['name']}\n"

            return output

        if tool == "list_commits":

            commits = json.loads(text)

            output = "# Latest Commits\n\n"

            for commit in commits[:5]:

                output += (
                    f"### {commit['commit']['message']}\n"
                    f"- Author: {commit['commit']['author']['name']}\n"
                    f"- Date: {commit['commit']['author']['date']}\n\n"
                )

            return output

        return text