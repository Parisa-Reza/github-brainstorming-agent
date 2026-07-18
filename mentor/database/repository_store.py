from surrealdb.errors import NotFoundError
class RepositoryStore:

    def __init__(self, db):
        self.db = db

    def get_by_url(
        self,
        repo_url: str,
    ):

        try:

                    result = self.db.query(
                        """
                        SELECT *
                        FROM repository
                        WHERE url = $url
                        LIMIT 1;
                        """,
                        {
                            "url": repo_url,
                        },
                    )

                    if result:
                        return result[0]

                    return None

        except NotFoundError:
                    return None

    def create_repository(
        self,
        repo_name: str,
        repo_url: str,
    ):

        return self.db.create(
            "repository",
            {
                "name": repo_name,
                "url": repo_url,
            },
        )

    def get_or_create_repository(
        self,
        repo_name: str,
        repo_url: str,
    ):

        existing = self.get_by_url(
            repo_url
        )

        if existing:
            return existing

        return self.create_repository(
            repo_name,
            repo_url,
        )
    
    def get_repository_id(
        self,
        repo_url: str,
    ):

        repository = self.get_by_url(
            repo_url
        )

        if repository:
            return repository["id"]

        return None