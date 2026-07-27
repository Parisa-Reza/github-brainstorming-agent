from pathlib import Path

from mentor.repositories.models import RepositoryDocument


class FileLoader:

    def load(self, file_path: Path) -> RepositoryDocument | None:

        try:
            content = file_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            return RepositoryDocument(
                path=str(file_path),
                content=content,
            )

        except Exception as exc:
            print(f"Failed to load {file_path}: {exc}")
            return None