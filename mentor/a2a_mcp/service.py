from chat.services.chat_service import ChatService


class MentorMCPService:

    def __init__(self):

        self.chat = ChatService()

    def ask_repository(
        self,
        question,
        repository_url,
        conversation_id="mcp",
    ):

        return self.chat.ask(
            question=question,
            repo_url=repository_url,
            conversation_id=conversation_id,
        )