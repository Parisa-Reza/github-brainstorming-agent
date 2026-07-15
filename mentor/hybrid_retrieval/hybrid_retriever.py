from mentor.graph.graph_service import (
    GraphService,
)

from mentor.hybrid_retrieval.graph_retriever import (
    GraphRetriever,
)

from mentor.hybrid_retrieval.context_builder import (
    ContextBuilder,
)

from mentor.retriever.retrieval_workflow import (
    RetrievalWorkflow
)

from mentor.hybrid_retrieval.entity_extractor import (
    EntityExtractor,
)

class HybridRetriever:

    def __init__(self):

        self.entity_extractor = (
            EntityExtractor()
        )

        self.vector_retriever = (
            RetrievalWorkflow()
        )

        self.graph_service = (
            GraphService()
        )

        graph = (
            self.graph_service.load_graph(
                "data/repositories/langchain/"
                "graphify-out/graph.json"
            )
        )

        self.graph_retriever = (
            GraphRetriever(graph)
        )

        self.context_builder = (
            ContextBuilder()
        )

    def retrieve(
        self,
        question: str,
    ):

        vector_results = (
            self.vector_retriever.retrieve(
                question
            )
        )

        entities = []

        for score, chunk in vector_results:

            entities.extend(
                self.entity_extractor.extract(
                    chunk["content"]
                )
            )

        graph_results = []

        for entity in entities:

            graph_results.extend(
                self.graph_retriever.retrieve(
                    entity
                )
            )



        context = (
            self.context_builder.build(
                vector_results,
                graph_results,
            )
        )

        return context