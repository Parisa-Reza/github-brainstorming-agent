from mentor.retriever.retrieval_workflow import (
    RetrievalWorkflow,
)


def main():

    workflow = (
        RetrievalWorkflow()
    )

    results = (
        workflow.retrieve(
            "How are prompts implemented in LangChain?"
        )
    )

    print()

    print(
        f"Retrieved {len(results)} chunks"
    )

    print()

    for score, chunk in results:

        print(
            f"Similarity Score: {score:.4f}"
        )

        print(
            f"File: {chunk['file_path']}"
        )

        print()

        print(
            chunk["content"][:500]
        )

        print()

        print(
            "=" * 80
        )


if __name__ == "__main__":
    main()