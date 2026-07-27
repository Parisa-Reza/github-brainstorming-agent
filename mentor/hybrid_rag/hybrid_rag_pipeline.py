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

        self.memory.save_message(
            session_id=session_id,
            role="user",
            content=question,
        )

        self.memory.save_message(
            session_id=session_id,
            role="assistant",
            content=answer,
        )

        return answer

