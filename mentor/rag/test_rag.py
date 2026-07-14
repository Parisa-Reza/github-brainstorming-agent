from mentor.rag.rag_pipeline import RagPipeline


def main():

    rag = RagPipeline()

    questions = [
        "How is authentication implemented in this repository?",
        "What library or mechanism handles it?",
        "What environment variables do I need to set up to get this application running?",
        "Where in the codebase is the MongoDB connection string (MONGO_URI) actually used?" ,
        "How does the code distinguish between a normal user and an admin?",
    ]

    for question in questions:

        print("=" * 80)
        print(question)
        print("=" * 80)

        answer = rag.ask(question)

        print(answer)
        print()


if __name__ == "__main__":
    main()