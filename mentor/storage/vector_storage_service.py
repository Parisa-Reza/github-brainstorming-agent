from mentor.database.surreal import get_db
from mentor.database.repository_store import RepositoryStore
from mentor.database.chunk_store import ChunkStore


class VectorStorageService:

    def __init__(self):

        self.db = get_db()

        self.repository_store = (
            RepositoryStore(self.db)
        )

        self.chunk_store = (
            ChunkStore(self.db)
        )

    def store(
        self,
        repo_name: str,
        repo_url: str,
        embeddings,
    ):

        repository = (
            self.repository_store
            .get_or_create_repository(
                repo_name,
                repo_url,
            )
        )

        repository_id = repository["id"]

        self.chunk_store.create_chunks(
            repository_id,
            embeddings,
        )

        return repository_id