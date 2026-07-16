from pathlib import Path


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
        )

    def get_graph_path(
        self,
        repo_url: str,
    ):

        repo_name = (
            self.get_repository_name(
                repo_url
            )
        )

        return (
            self.BASE_DIR
            / repo_name
            / "graphify-out"
            / "graph.json"
        )