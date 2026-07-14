from mentor.repositories.repository_service import RepositoryService
from mentor.chunking.chunking_service import ChunkingService


def main():

    repo_service = RepositoryService()

    documents = repo_service.ingest(
        "https://github.com/langchain-ai/langchain"
    )

    chunking_service = ChunkingService()

    chunks = chunking_service.chunk_documents(
        documents
    )

    print(
        f"Documents: {len(documents)}"
    )

    print(
        f"Chunks: {len(chunks)}"
    )

    print()

    first_chunk = chunks[0]

    print(first_chunk.file_path)

    print("-" * 80)

    print(first_chunk.content[:500])


if __name__ == "__main__":
    main()