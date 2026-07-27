from mentor.chunking.chunk_service import ChunkService


class ChunkingService:

    def __init__(self):
        self.chunk_service = ChunkService()

    def chunk_documents(
        self,
        documents,
    ):
        chunks = []

        for document in documents:
            chunks.extend(
                self.chunk_service.chunk_document(
                    document
                )
            )

        return chunks