from pathlib import Path

from mentor.repositories.file_discovery import FileDiscovery


def main():
    repository_path = Path("data/repositories/langchain")

    discovery = FileDiscovery()

    files = discovery.discover(repository_path)

    print(f"Found {len(files)} files")

    for file in files[:10]:
        print(file)


if __name__ == "__main__":
    main()