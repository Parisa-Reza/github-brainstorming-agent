from dataclasses import dataclass


@dataclass
class DocumentChunk:
    file_path: str
    chunk_index: int
    content: str