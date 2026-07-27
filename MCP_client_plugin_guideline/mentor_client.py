import os

from dotenv import load_dotenv

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


class MentorClient:

    def __init__(self):

        self.server = StdioServerParameters(
            command=os.environ["MENTOR_PYTHON"],
            args=[
                "-m",
                "mentor.a2a_mcp.a2a_mcp_server",
            ],
            cwd=os.environ["MENTOR_PROJECT_PATH"],
        )

    async def ask_repository(
        self,
        repository_url: str,
        question: str,
    ) -> str:

        async with stdio_client(self.server) as (read, write):
            async with ClientSession(read, write) as session:

                await session.initialize()

                result = await session.call_tool(
                    "ask_repository",
                    {
                        "repository_url": repository_url,
                        "question": question,
                    },
                )

                if result.isError:
                    raise Exception(result.content[0].text)

                return result.content[0].text