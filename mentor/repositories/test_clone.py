from mentor.repositories.github_service import GithubService


def main():

    service = GithubService()

    path = service.clone_repository(
        "https://github.com/langchain-ai/langchain"
    )

    print(path)


if __name__ == "__main__":
    main()