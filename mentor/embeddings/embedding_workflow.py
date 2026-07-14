from mentor.embeddings.models import ChunkEmbedding
from mentor.embeddings.embedding_service import (
    EmbeddingService,
)


class EmbeddingWorkflow:

    def __init__(self):
        self.embedding_service = (
            EmbeddingService()
        )

    def generate_embeddings(
        self,
        chunks,
    ):

        embeddings = []

        for chunk in chunks:

            vector = (
                self.embedding_service
                .generate_embedding(
                    chunk.content
                )
            )

            embeddings.append(
                ChunkEmbedding(
                    file_path=chunk.file_path,
                    chunk_index=chunk.chunk_index,
                    content=chunk.content,
                    embedding=vector,
                )
            )

        return embeddings