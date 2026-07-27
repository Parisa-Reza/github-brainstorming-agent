from urllib.parse import urlparse


class RepositoryParser:

    def parse(
        self,
        repo_url: str,
    ):

        path = urlparse(repo_url).path.strip("/")

        owner, repo = path.split("/")[:2]

        return owner, repo