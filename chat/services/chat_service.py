from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

from mentor.llm.answer_generator import (
    AnswerGenerator,
)

from mentor.memory.short_term_memory.short_term_memory import (
    ShortTermMemory,
)


class ChatService:

    def __init__(self):

        self.retriever = HybridRetriever()

        self.generator = AnswerGenerator()

        self.memory = ShortTermMemory()

    def ask(
        self,
        question: str,
        repo_url: str,
        conversation_id: str,
    ):

        # Load conversation history
        history = self.memory.get_history(
            conversation_id
        )

        # Retrieve repository context
        context = self.retriever.retrieve(
            question,
            repo_url,
        )

        # Generate answer
        answer = self.generator.generate(
            question=question,
            context=context,
            history=history,
        )

        # Save conversation
        self.memory.save_user_message(
            conversation_id,
            question,
        )

        self.memory.save_assistant_message(
            conversation_id,
            answer,
        )

        return answer

