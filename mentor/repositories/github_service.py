from pathlib import Path
from git import Repo


class GithubService:

    BASE_DIR = Path("data/repositories")

    def clone_repository(self, repo_url: str):

        repo_name = repo_url.rstrip("/").split("/")[-1]

        target_path = self.BASE_DIR / repo_name

        if target_path.exists():
            return target_path

        Repo.clone_from(
            repo_url,
            target_path,
        )

        return target_path