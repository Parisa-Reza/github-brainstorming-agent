from pathlib import Path


class FileDiscovery:

    SUPPORTED_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".go",
        ".java",
        ".md",
    }

    IGNORED_DIRECTORIES = {
        ".git",
        "node_modules",
        "__pycache__",
        "venv",
        ".venv",
    }

    def discover(self, repository_path: Path) -> list[Path]:
        files = []

        for file_path in repository_path.rglob("*"):

            if not file_path.is_file():
                continue

            if any(
                ignored in file_path.parts
                for ignored in self.IGNORED_DIRECTORIES
            ):
                continue

            if file_path.suffix not in self.SUPPORTED_EXTENSIONS:
                continue

            files.append(file_path)

        return files