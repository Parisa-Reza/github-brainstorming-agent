
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class GitHubMCPClient:
    """GitHub MCP in Docker through MITM proxy + mitm CA trust."""

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN") or os.getenv(
            "GITHUB_PERSONAL_ACCESS_TOKEN", ""
        )
        if not token:
            raise RuntimeError(
                "Set GITHUB_TOKEN (or GITHUB_PERSONAL_ACCESS_TOKEN) in the environment"
            )

        proxy = (
            os.getenv("HTTPS_PROXY")
            or os.getenv("https_proxy")
            or os.getenv("HTTP_PROXY")
            or os.getenv("http_proxy")
            or "http://192.168.1.235:8088"
        )

        # Use the mitm CA file itself (most reliable inside containers)
        ca_host = "/usr/local/share/ca-certificates/mitmproxy.crt"
        if not os.path.isfile(ca_host):
            raise RuntimeError(f"MITM CA not found: {ca_host}")

        ca_container = "/mitm.crt"

        self.server = StdioServerParameters(
            command="docker",
            args=[
                "run",
                "-i",
                "--rm",
                "-e",
                f"GITHUB_PERSONAL_ACCESS_TOKEN={token}",
                "-e",
                f"HTTP_PROXY={proxy}",
                "-e",
                f"HTTPS_PROXY={proxy}",
                "-e",
                f"http_proxy={proxy}",
                "-e",
                f"https_proxy={proxy}",
                "-e",
                "NO_PROXY=localhost,127.0.0.1",
                "-e",
                "no_proxy=localhost,127.0.0.1",
                "-v",
                f"{ca_host}:{ca_container}:ro",
                # Go (github-mcp-server) reads SSL_CERT_FILE
                "-e",
                f"SSL_CERT_FILE={ca_container}",
                "ghcr.io/github/github-mcp-server:latest",
                "stdio",
            ],
        )

    async def list_tools(self):
        async with stdio_client(self.server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await session.list_tools()

    async def call_tool(self, tool_name, arguments):
        async with stdio_client(self.server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await session.call_tool(tool_name, arguments)




# import os

# from mcp import (
#     ClientSession,
#     StdioServerParameters,
# )

# from mcp.client.stdio import (
#     stdio_client,
# )


# class GitHubMCPClient:

#     def __init__(self):

#         self.server = (
#             StdioServerParameters(

#                 command="docker",

#                 # args=[
#                 #     "run",
#                 #     "-i",
#                 #     "--rm",
#                 #     "-e",
#                 #     f"GITHUB_PERSONAL_ACCESS_TOKEN={os.getenv('GITHUB_TOKEN')}",
#                 #     "ghcr.io/github/github-mcp-server:latest",
#                 #     "stdio",
#                 # ],

#                 args=[
#                     "run",
#                     "-i",
#                     "--rm",

#                     "-e", f"GITHUB_PERSONAL_ACCESS_TOKEN={os.getenv('GITHUB_TOKEN')}",
#                     "-e", "HTTP_PROXY=",
#                     "-e", "HTTPS_PROXY=",
#                     "-e", "NO_PROXY=",
#                     "-e", "http_proxy=",
#                     "-e", "https_proxy=",
#                     "-e", "no_proxy=",


#                     "ghcr.io/github/github-mcp-server:latest",
#                     "stdio",
#                 ]
#             )
#         )

#     async def list_tools(self):

#         async with stdio_client(
#             self.server,
#         ) as (
#             read,
#             write,
#         ):

#             async with ClientSession(
#                 read,
#                 write,
#             ) as session:

#                 await session.initialize()

#                 return await session.list_tools()

#     async def call_tool(
#         self,
#         tool_name,
#         arguments,
#     ):

#         async with stdio_client(
#             self.server,
#         ) as (
#             read,
#             write,
#         ):

#             async with ClientSession(
#                 read,
#                 write,
#             ) as session:

#                 await session.initialize()

#                 return await session.call_tool(
#                     tool_name,
#                     arguments,
#                 )