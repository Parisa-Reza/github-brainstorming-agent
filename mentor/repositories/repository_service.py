from mentor.repositories.github_service import GithubService
from mentor.repositories.file_discovery import FileDiscovery
from mentor.repositories.file_loader import FileLoader


class RepositoryService:

    def __init__(self):
        self.github_service = GithubService()
        self.file_discovery = FileDiscovery()
        self.file_loader = FileLoader()

    def ingest(self, repo_url: str):

        repository_path = self.github_service.clone_repository(
            repo_url
        )

        files = self.file_discovery.discover(
            repository_path
        )

        documents = []

        for file_path in files:

            document = self.file_loader.load(
                file_path
            )

            if document:
                documents.append(document)

        return documents