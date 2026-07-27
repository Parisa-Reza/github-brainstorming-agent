from mentor.llm.llm_service import (
    LLMService,
)


class MemoryExtractor:

    def __init__(self):

        self.llm = (
            LLMService()
            .get_llm()
        )

    def extract(

        self,

        user_message,

        assistant_message,

    ):

        prompt = f"""
You are a memory extraction system.

Read this conversation.

User:
{user_message}

Assistant:
{assistant_message}

Only extract information that will be useful in future conversations.

Examples

- User prefers Python.
- User uses Django.
- User is working on Hybrid RAG.
- User likes concise explanations.
- User uses SurrealDB.

Ignore

- Greetings
- Thanks
- One-time questions
- Temporary information

Return one memory per line.

If nothing is worth remembering return ONLY

NONE
"""

        response = self.llm.invoke(
            prompt
        )

        text = self._response_text(
            response.content
        ).strip()

        if text == "NONE":

            return []

        memories = []

        for line in text.split("\n"):

            line = line.strip()

            if line:

                memories.append(
                    line
                )

        return memories

    def _response_text(
        self,
        content,
    ):

        if isinstance(content, str):

            return content

        if isinstance(content, list):

            parts = []

            for block in content:

                if isinstance(block, str):

                    parts.append(block)

                elif isinstance(block, dict):

                    text = block.get("text")

                    if isinstance(text, str):

                        parts.append(text)

            return "\n".join(parts)

        return str(content)
