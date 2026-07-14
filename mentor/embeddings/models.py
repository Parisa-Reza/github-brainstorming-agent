from dataclasses import dataclass

from mentor.chunking.models import DocumentChunk


@dataclass
class ChunkEmbedding:
    file_path: str
    chunk_index: int
    content: str
    embedding: list[float]