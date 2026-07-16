
from mentor.llm.response_parser import (
    ResponseParser,
)

from mentor.llm.llm_service import (
    LLMService,
)

from mentor.llm.prompt_builder import (
    PromptBuilder,
)


class AnswerGenerator:

    def __init__(self):

        self.llm = (
            LLMService().get_llm()
        )

        self.prompt_builder = (
            PromptBuilder()
        )

        self.parser = (
            ResponseParser()
        )

    def generate(
    self,
    question: str,
    context: str,
    ):

        prompt = (
            self.prompt_builder
            .build()
            .format(
                context=context,
                question=question,
            )
        )

        response = (
            self.llm.invoke(
                prompt
            )
        )

        return self.parser.parse(
            response
        )
