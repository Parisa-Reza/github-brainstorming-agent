import os

from mcp import ClientSession
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client


class GitHubMCPClient:

    def __init__(self):

        self.server = StdioServerParameters(

            command="docker",

            args=[
                "run",
                "-i",
                "--rm",
                "-e",
                f"GITHUB_PERSONAL_ACCESS_TOKEN={os.getenv('GITHUB_TOKEN')}",
                "ghcr.io/github/github-mcp-server:latest",
                "stdio",
            ],
        )

    async def list_tools(self):

        async with stdio_client(
            self.server
        ) as (read, write):

            async with ClientSession(
                read,
                write,
            ) as session:

                await session.initialize()

                return await session.list_tools()