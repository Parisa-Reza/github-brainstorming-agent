from sentence_transformers import (
    SentenceTransformer,
)

import sys
from huggingface_hub.utils import disable_progress_bars

# Disable Hugging Face progress bars globally
disable_progress_bars()

class EmbeddingService:

    _model = None

    def __init__(self):

        print("EmbeddingService initialized", file=sys.stderr)

        if EmbeddingService._model is None:

            print("Loading embedding model...", file=sys.stderr)

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