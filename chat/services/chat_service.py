
from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

from mentor.llm.answer_generator import (
    AnswerGenerator,
)


class ChatService:

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
        repo_url: str,
    ):

        context = (
            self.retriever.retrieve(
                question,
                repo_url,
            )
        )

        return (
            self.generator.generate(
                question,
                context,
            )
        )
