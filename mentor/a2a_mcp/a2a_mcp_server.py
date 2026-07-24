from mcp.server.fastmcp import FastMCP

from .tools import service

mcp = FastMCP("GitHub Engineering Mentor")

@mcp.tool()
async def ask_repository(
    repository_url: str,
    question: str,
) -> str:
    """
    Ask questions about a repository.
    """

    return await service.ask_repository(
        question=question,
        repository_url=repository_url,
    )


if __name__ == "__main__":
    print("Starting GitHub Engineering Mentor MCP Server...")
    mcp.run(transport="stdio")