from langchain_core.prompts import (
    PromptTemplate,
)


class PromptBuilder:

    def build(self):

        template = """
You are a senior software engineer.

Answer ONLY using the repository context.

If the answer cannot be found in the context, say:

"I could not find enough information in the repository."

Context:
{context}

Question:
{question}

Answer:
"""

        return PromptTemplate(
            template=template,
            input_variables=[
                "context",
                "question",
            ],
        )

