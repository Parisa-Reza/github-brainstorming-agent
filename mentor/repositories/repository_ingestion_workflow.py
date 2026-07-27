from pathlib import Path

from mentor.repositories.repository_service import (
    RepositoryService,
)

from mentor.chunking.chunk_service import (
    ChunkService,
)

from mentor.embeddings.embedding_workflow import (
    EmbeddingWorkflow,
)

from mentor.storage.vector_storage_service import (
    VectorStorageService,
)


class RepositoryIngestionWorkflow:

    def __init__(self):

        self.repository_service = (
            RepositoryService()
        )

        self.chunk_service = (
            ChunkService()
        )

        self.embedding_workflow = (
            EmbeddingWorkflow()
        )

        self.storage_service = (
            VectorStorageService()
        )

    def ingest(
        self,
        repo_url: str,
    ):

        documents = (
            self.repository_service.ingest(
                repo_url
            )
        )

        chunks = []

        for document in documents:

            chunks.extend(
                self.chunk_service.chunk_document(
                    document
                )
            )

        embeddings = (
            self.embedding_workflow
            .generate_embeddings(
                chunks
            )
        )

        repo_name = (
            Path(repo_url.rstrip("/"))
            .name
        )

        repository_id = (
            self.storage_service.store(
                repo_name=repo_name,
                repo_url=repo_url,
                embeddings=embeddings,
            )
        )

        return repository_id