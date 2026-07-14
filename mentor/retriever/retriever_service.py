from mentor.database.surreal import get_db


class RetrieverService:

    def __init__(self):
        self.db = get_db()

    def get_chunks(self):

        chunks = self.db.select(
            "chunk"
        )

        return chunks