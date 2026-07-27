from mentor.memory.short_term_memory.conversation_store import (
    ConversationStore,
)


class ShortTermMemory:

    def __init__(self):

        self.store = ConversationStore()

    def save_user_message(
        self,
        conversation_id,
        message,
    ):

        self.store.append_message(
            conversation_id,
            "user",
            message,
        )

    def save_assistant_message(
        self,
        conversation_id,
        message,
    ):

        self.store.append_message(
            conversation_id,
            "assistant",
            message,
        )

    def get_history(
        self,
        conversation_id,
    ):

        # return self.store.get_messages(
        #     conversation_id
        # )
            messages = self.store.get_messages(
                conversation_id
            )

            return messages[-8:]

    def clear(
        self,
        conversation_id,
    ):

        self.store.clear(
            conversation_id
        )