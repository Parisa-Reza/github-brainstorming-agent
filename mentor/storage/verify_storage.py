from mentor.database.surreal import get_db


def main():

    db = get_db()

    repositories = db.select("repository")

    print(f"Repositories: {len(repositories)}")

    chunks = db.select("chunk")

    print(f"Chunks: {len(chunks)}")

    print()

    if chunks:
        print("Sample Chunk:")
        print(chunks[0])


if __name__ == "__main__":
    main()