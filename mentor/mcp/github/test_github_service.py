from mentor.mcp.github.github_service import (
    GitHubService,
)
import os

print(os.getenv("GITHUB_TOKEN"))

service = GitHubService()

result = service.get_file_contents(

    owner="Parisa-Reza",

    repo="tech-semantic-search",

    path="README.md",

)

print()

print(result)