class ChunkStore:

    def __init__(self, db):
        self.db = db

    def create_chunk(
        self,
        repository_id: str,
        file_path: str,
        chunk_index: int,
        content: str,
        embedding: list[float],
    ):

        return self.db.create(
            "chunk",
            {
                "repository_id": repository_id,
                "file_path": file_path,
                "chunk_index": chunk_index,
                "content": content,
                "embedding": embedding,
            },
        )

    def create_chunks(
        self,
        repository_id: str,
        embeddings,
    ):

        for embedding in embeddings:

            self.create_chunk(
                repository_id=repository_id,
                file_path=embedding.file_path,
                chunk_index=embedding.chunk_index,
                content=embedding.content,
                embedding=embedding.embedding,
            )