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

        # Loading the same URL again must replace its index.  Appending left
        # stale chunks from an earlier (and, before owner-scoped checkouts,
        # potentially different) repository available to retrieval.
        self.chunk_store.delete_chunks_by_repository(
            repository_id
        )

        self.chunk_store.create_chunks(
            repository_id,
            embeddings,
        )

        return repository_id
