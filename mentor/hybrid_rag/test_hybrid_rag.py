from mentor.hybrid_rag.hybrid_rag_pipeline import (
    RAGPipeline,
)

QUESTION = (
    "how prompt template is implemented in langchain?"
)

pipeline = RAGPipeline()

answer = pipeline.ask(
    QUESTION
)

print()
print("=" * 80)
print(answer)
print("=" * 80)

