from pathlib import Path
from git import Repo

from mentor.repositories.repository_locator import RepositoryLocator


class GithubService:

    BASE_DIR = Path("data/repositories")

    def __init__(self):
        self.repository_locator = RepositoryLocator()

    def clone_repository(self, repo_url: str):

        target_path = self.repository_locator.get_repository_path(repo_url)

        if target_path.exists():
            return target_path

        target_path.parent.mkdir(parents=True, exist_ok=True)

        Repo.clone_from(
            repo_url,
            target_path,
        )

        return target_path
