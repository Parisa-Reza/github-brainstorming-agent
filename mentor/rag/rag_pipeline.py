from mentor.rag.prompts import (
    RAG_PROMPT,
)

from mentor.rag.chains import (
    get_llm,
)

from mentor.retriever.retrieval_workflow import (
    RetrievalWorkflow,
)


class RagPipeline:

    def __init__(self):

        self.retriever = (
            RetrievalWorkflow()
        )

        self.llm = get_llm()

        self.chain = (
            RAG_PROMPT | self.llm # this is LCEL
        )

    def ask(
        self,
        question: str,
    ):

        chunks = (
            self.retriever.retrieve(
                question
            )
        )

        context = "\n\n".join(
            chunk["content"]
            for _, chunk in chunks
        )

        print("\nRETRIEVED CHUNKS\n")

        for score, chunk in chunks:
            print(f"Score: {score:.4f}")
            print(f"File: {chunk['file_path']}")
            print("-" * 80)

        response = self.chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return response.content