from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

from mentor.llm.answer_generator import (
    AnswerGenerator,
)


retriever = (
    HybridRetriever()
)

generator = (
    AnswerGenerator()
)


class ChatService:

    def ask(
        self,
        question: str,
    ):

        context = (
            retriever.retrieve(
                question
            )
        )

        return (
            generator.generate(
                question,
                context,
            )
        )