
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
    RetrievalWorkflow,
)

from mentor.hybrid_retrieval.entity_extractor import (
    EntityExtractor,
)

from mentor.database.surreal import (
    get_db,
)

from mentor.database.repository_store import (
    RepositoryStore,
)

from mentor.repositories.repository_locator import (
    RepositoryLocator,
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

        self.context_builder = (
            ContextBuilder()
        )

        self.repository_store = (
            RepositoryStore(
                get_db()
            )
        )

        self.repository_locator = (
            RepositoryLocator()
        )

    def retrieve(
        self,
        question: str,
        repo_url: str,
    ):

        repository_id = (
            self.repository_store
            .get_repository_id(
                repo_url
            )
        )

        if not repository_id:

            return (
                "Repository has not been indexed."
            )

        vector_results = (
            self.vector_retriever.retrieve(
                question,
                repository_id,
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

        graph_path = (
            self.repository_locator
            .get_graph_path(
                repo_url
            )
        )

        if graph_path.exists():

            graph = (
                self.graph_service.load_graph(
                    graph_path
                )
            )

            graph_retriever = (
                GraphRetriever(
                    graph
                )
            )

            for entity in entities:

                graph_results.extend(
                    graph_retriever.retrieve(
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


