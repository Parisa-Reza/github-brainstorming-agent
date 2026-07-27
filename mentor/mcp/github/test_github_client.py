import asyncio

from mentor.mcp.github.github_client import (
    GitHubMCPClient,
)


async def main():

    client = GitHubMCPClient()

    tools = await client.list_tools()

    print()

    print("Available Tools")

    print("----------------")

    for tool in tools.tools:

        print(tool.name)


asyncio.run(main())