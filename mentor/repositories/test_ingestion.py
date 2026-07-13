from mentor.repositories.repository_service import RepositoryService


def main():

    service = RepositoryService()

    documents = service.ingest(
        "https://github.com/langchain-ai/langchain"
    )

    print(f"Loaded {len(documents)} documents")

    print()

    for document in documents[:5]:
        print(document.path)
        print("-" * 50)


if __name__ == "__main__":
    main()