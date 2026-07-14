from langchain_core.prompts import PromptTemplate


RAG_PROMPT = PromptTemplate(
    input_variables=[
        "context",
        "question",
    ],
    template="""
You are a senior software engineering mentor. You explain everything in simple and easy words.

Use only the repository context.

Context:
{context}

Question:
{question}pro

Answer:
"""
)