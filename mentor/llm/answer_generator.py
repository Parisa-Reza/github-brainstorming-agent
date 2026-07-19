
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
    history: list,
    ):

        history_text = ""

        for message in history:

            history_text += (
                f"{message['role']}: "
                f"{message['content']}\n"
            )

        prompt = (
            self.prompt_builder
            .build()
            .format(
                history=history_text,
                context=context,
                question=question,
            )
        )

        print("\n========== PROMPT ==========\n")
        print(prompt)
        print("\n============================\n")

        response = (
            self.llm.invoke(
                prompt
            )
        )

        return self.parser.parse(
            response
        )
