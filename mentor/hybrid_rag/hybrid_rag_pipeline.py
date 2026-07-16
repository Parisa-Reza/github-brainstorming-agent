from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

from mentor.llm.answer_generator import (
    AnswerGenerator,
)


class RAGPipeline:

    def __init__(self):

        self.retriever = (
            HybridRetriever()
        )

        self.generator = (
            AnswerGenerator()
        )

    def ask(
        self,
        question: str,
    ):

        context = (
            self.retriever.retrieve(
                question
            )
        )

        answer = (
            self.generator.generate(
                question=question,
                context=context,
            )
        )

        return answer

