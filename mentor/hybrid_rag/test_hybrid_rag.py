from mentor.hybrid_rag.hybrid_rag_pipeline import (
    RAGPipeline,
)

QUESTION = (
     "What is PromptTemplate?"
)

pipeline = (
    RAGPipeline()
)

answer = pipeline.ask(
    QUESTION
)

print()
print("=" * 80)
print(answer)
print("=" * 80)
print()