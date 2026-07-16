from sentence_transformers import (
    SentenceTransformer,
)


class EmbeddingService:

    _model = None

    def __init__(self):

        print("EmbeddingService initialized")

        if EmbeddingService._model is None:

            print("Loading embedding model...")

            EmbeddingService._model = (
                SentenceTransformer(
                    "all-MiniLM-L6-v2"
                )
            )

        self.model = (
            EmbeddingService._model
        )

    def generate_embedding(
        self,
        text: str,
    ) -> list[float]:

        return self.model.encode(
            text
        ).tolist()