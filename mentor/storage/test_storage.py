from mentor.repositories.repository_service import (
    RepositoryService,
)

from mentor.chunking.chunking_service import (
    ChunkingService,
)

from mentor.embeddings.embedding_workflow import (
    EmbeddingWorkflow,
)

from mentor.storage.vector_storage_service import (
    VectorStorageService,
)


def main():

    repo_url = (
        "https://github.com/langchain-ai/langchain"
    )

    print("Loading repository...")

    repository_service = (
        RepositoryService()
    )

    documents = (
        repository_service.ingest(
            repo_url
        )
    )

    print(
        f"Documents: {len(documents)}"
    )

    print()

    chunking_service = (
        ChunkingService()
    )

    chunks = (
        chunking_service.chunk_documents(
            documents
        )
    )

    print(
        f"Chunks: {len(chunks)}"
    )

    print()

    embedding_workflow = (
        EmbeddingWorkflow()
    )

    embeddings = (
        embedding_workflow.generate_embeddings(
            chunks[:10]
        )
    )

    print(
        f"Embeddings: {len(embeddings)}"
    )

    print()

    storage_service = (
        VectorStorageService()
    )

    repository_id = (
        storage_service.store(
            repo_name="langchain",
            repo_url=repo_url,
            embeddings=embeddings,
        )
    )

    print()

    print(
        f"Repository Stored: {repository_id}"
    )

    print(
        f"Stored {len(embeddings)} chunks"
    )


if __name__ == "__main__":
    main()