from dataclasses import dataclass


@dataclass
class RepositoryDocument:
    path: str
    content: str