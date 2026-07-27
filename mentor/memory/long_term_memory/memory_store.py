from mentor.database.surreal import get_db


class MemoryStore:

    def __init__(self):

        self.db = get_db()

    def save_memory(
        self,
        conversation_id,
        fact,
    ):

        return self.db.create(
            "memory",
            {
                "conversation_id": conversation_id,
                "fact": fact,
            },
        )

    def get_memories(
        self,
        conversation_id,
    ):

        result = self.db.query(
            """
            SELECT *
            FROM memory
            WHERE conversation_id = $conversation_id;
            """,
            {
                "conversation_id": conversation_id,
            },
        )

        if not result:
            return []

        return result

    def delete_memories(
        self,
        conversation_id,
    ):

        self.db.query(
            """
            DELETE memory
            WHERE conversation_id = $conversation_id;
            """,
            {
                "conversation_id": conversation_id,
            },
        )