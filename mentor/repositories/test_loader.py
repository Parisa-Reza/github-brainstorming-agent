from pathlib import Path

from mentor.repositories.file_loader import FileLoader


def main():

    loader = FileLoader()

    file_path = Path(
        "data/repositories/langchain/libs/core/langchain_core/prompts/base.py"
    )

    document = loader.load(file_path)

    if document:
        print(document.path)
        print("-" * 80)
        print(document.content[:1000])


if __name__ == "__main__":
    main()