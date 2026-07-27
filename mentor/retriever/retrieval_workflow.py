from mentor.embeddings.embedding_service import (
    EmbeddingService,
)

from mentor.retriever.similarity import (
    SimilarityService,
)

from mentor.retriever.retriever_service import (
    RetrieverService,
)


class RetrievalWorkflow:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.retriever_service = (
            RetrieverService()
        )

    def retrieve(
        self,
        question: str,
        repository_id: str,
        top_k: int = 3,
    ):

        query_embedding = (
            self.embedding_service
            .generate_embedding(
                question
            )
        )

        chunks = (
            self.retriever_service
            .get_chunks( repository_id)
        )

        scored_chunks = []

        for chunk in chunks:

            score = (
                SimilarityService
                .cosine_similarity(
                    query_embedding,
                    chunk["embedding"],
                )
            )

            scored_chunks.append(
                (
                    score,
                    chunk,
                )
            )

        scored_chunks.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return scored_chunks[:top_k] # default : top 3 results