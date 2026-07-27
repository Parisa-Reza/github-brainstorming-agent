from mentor.repositories.repository_service import (
    RepositoryService,
)

from mentor.chunking.chunking_service import (
    ChunkingService,
)

from mentor.embeddings.embedding_workflow import (
    EmbeddingWorkflow,
)


def main():

    print("Loading repository...")

    repository_service = (
        RepositoryService()
    )

    documents = (
        repository_service.ingest(
            "https://github.com/langchain-ai/langchain"
        )
    )

    print(
        f"Documents loaded: {len(documents)}"
    )

    print()

    print("Creating chunks...")

    chunking_service = (
        ChunkingService()
    )

    chunks = (
        chunking_service.chunk_documents(
            documents
        )
    )

    print(
        f"Chunks created: {len(chunks)}"
    )

    print()

    print("Generating embeddings...")

    embedding_workflow = (
        EmbeddingWorkflow()
    )

    embeddings = (
        embedding_workflow.generate_embeddings(
            chunks[:5]
        )
    )

    print(
        f"Embeddings generated: {len(embeddings)}"
    )

    print()

    first_embedding = embeddings[0]

    print(
        f"File: {first_embedding.file_path}"
    )

    print(
        f"Chunk Index: {first_embedding.chunk_index}"
    )

    print(
        f"Embedding Dimension: {len(first_embedding.embedding)}"
    )

    print()

    print(
        first_embedding.embedding[:10]
    )


if __name__ == "__main__":
    main()