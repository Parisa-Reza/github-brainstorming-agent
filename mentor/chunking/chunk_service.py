from mentor.chunking.models import DocumentChunk
from mentor.repositories.models import RepositoryDocument


class ChunkService:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_document(
        self,
        document: RepositoryDocument,
    ) -> list[DocumentChunk]:

        chunks = []

        content = document.content

        start = 0
        index = 0

        while start < len(content):

            end = start + self.chunk_size

            chunk_content = content[start:end]

            chunks.append(
                DocumentChunk(
                    file_path=document.path,
                    chunk_index=index,
                    content=chunk_content,
                )
            )

            start += (
                self.chunk_size
                - self.chunk_overlap
            )

            index += 1

        return chunks