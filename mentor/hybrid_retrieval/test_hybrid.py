
from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

QUESTION = (
    "OutputParserException"
)

retriever = HybridRetriever()

print("\nVECTOR RESULTS")
print("=" * 80)

vector_results = (
    retriever.vector_retriever.retrieve(
        QUESTION
    )
)

for score, chunk in vector_results:

    print(
        f"Score: {score:.4f}"
    )

    print(
        chunk["content"][:300]
    )

    print()

print("\nGRAPH RESULTS")
print("=" * 80)

graph_results = (
    retriever.graph_retriever.retrieve(
        QUESTION
    )
)

for node in graph_results:

    print(
        node["label"]
    )

print()

print("\nHYBRID CONTEXT")
print("=" * 80)

context = retriever.retrieve(
    QUESTION
)

print(context[:3000])