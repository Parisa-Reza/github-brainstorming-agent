from mentor.database.surreal import get_db

import uuid


class ConversationStore:

    def __init__(self):

        self.db = get_db()

    def create_conversation(
        self,
        conversation_id,
    ):

        return self.db.create(
            "conversation",
            {
                "session_id": conversation_id,
                "messages": [],
            },
        )

    def get_conversation(
        self,
        conversation_id,
    ):

        result = self.db.query(
            """
            SELECT *
            FROM conversation
            WHERE session_id = $session_id
            LIMIT 1;
            """,
            {
                "session_id": conversation_id,
            },
        )

        if result:

            return result[0]

        return None

    def append_message(
        self,
        conversation_id,
        role,
        content,
    ):

        conversation = self.get_conversation(
            conversation_id
        )

        if conversation is None:

            conversation = self.create_conversation(
                conversation_id
            )

        messages = conversation.get(
            "messages",
            [],
        )

        messages.append(
            {
                "role": role,
                "content": content,
            }
        )

        self.db.merge(
            conversation["id"],
            {
                "messages": messages,
            },
        )

    def get_messages(
        self,
        conversation_id,
    ):

        conversation = self.get_conversation(
            conversation_id
        )

        if conversation is None:

            return []

        return conversation.get(
            "messages",
            [],
        )

    def clear(
        self,
        conversation_id,
    ):

        conversation = self.get_conversation(
            conversation_id
        )

        if conversation:

            self.db.delete(
                conversation["id"]
            )