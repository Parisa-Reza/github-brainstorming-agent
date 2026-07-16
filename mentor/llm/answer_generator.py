from mentor.llm.prompt_builder import (
    PromptBuilder,
)

from mentor.llm.llm_service import (
    LLMService,
)


class AnswerGenerator:

    def __init__(self):

        self.prompt = (
            PromptBuilder()
            .build()
        )

        self.llm = (
            LLMService()
            .get_llm()
        )

        self.chain = (
            self.prompt
            | self.llm
        )

    def generate(
        self,
        question: str,
        context: str,
    ):

        response = (
            self.chain.invoke(
                {
                    "question": question,
                    "context": context,
                }
            )
        )

        return response.content