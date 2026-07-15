from mentor.hybrid_retrieval.hybrid_retriever import (
    HybridRetriever,
)

from mentor.llm.prompt_builder import (
    PromptBuilder,
)

from mentor.llm.llm_service import (
    LLMService,
)


class RAGPipeline:

    def __init__(self):

        self.retriever = (
            HybridRetriever()
        )

        self.prompt_builder = (
            PromptBuilder()
        )

        self.llm_service = (
            LLMService()
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

        prompt = (
            self.prompt_builder.build(
                question,
                context,
            )
        )

        answer = (
            self.llm_service.generate(
                prompt
            )
        )

        return answer