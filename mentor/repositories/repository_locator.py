from pathlib import Path
from urllib.parse import urlparse


class RepositoryLocator:

    BASE_DIR = Path(
        "data/repositories"
    )

    def get_repository_name(
        self,
        repo_url: str,
    ):

        return (
            repo_url
            .rstrip("/")
            .split("/")[-1]
            .removesuffix(".git")
        )

    def get_repository_path(
        self,
        repo_url: str,
    ):
        """Return a checkout path that cannot collide with another owner.

        Repositories were previously stored under just their name.  For
        example, ``bongodev/project`` and ``Parisa-Reza/project`` both used
        ``data/repositories/project`` and the first clone was silently reused.
        """
        path_parts = urlparse(repo_url).path.strip("/").split("/")

        if len(path_parts) < 2:
            raise ValueError("A GitHub repository URL must include owner and repository.")

        owner, repo = path_parts[:2]

        return self.BASE_DIR / owner / repo.removesuffix(".git")

    def get_graph_path(
        self,
        repo_url: str,
    ):

        return (
            self.get_repository_path(
                repo_url
            )
            / "graphify-out"
            / "graph.json"
        )
