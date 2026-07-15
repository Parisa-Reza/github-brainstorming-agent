class PromptBuilder:

    def build(
        self,
        question: str,
        context: str,
    ):

        return f"""
You are a senior software engineer.

Answer ONLY using the repository context below.

If the answer is not present in the context,
say:

"I could not find enough information in the repository."

Repository Context:

{context}

Question:

{question}

Answer:
"""