import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server = StdioServerParameters(
        command="python",
        args=[
            "-m",
            "mentor.a2a_mcp.a2a_mcp_server",
        ],
    )

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
            "ask_repository",
            {
                "repository_url": "https://github.com/Parisa-Reza/PC-health-checking-MCP",
                "question": "How many branches are there?",
            },
        )

            print(result)


asyncio.run(main())