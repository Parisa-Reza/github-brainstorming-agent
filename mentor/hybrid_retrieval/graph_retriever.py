
from mentor.graph.graph_query import GraphQuery

from mentor.hybrid_retrieval.query_keywords import (
    QueryKeywords,
)


class GraphRetriever:

    def __init__(
        self,
        graph_data,
    ):
        self.query = GraphQuery(
            graph_data
        )

        self.keyword_extractor = (
            QueryKeywords()
        )

    def retrieve(
        self,
        question: str,
        limit: int = 10,
    ):

        keywords = (
            self.keyword_extractor.extract(
                question
            )
        )

        matches = []

        for keyword in keywords:

            nodes = (
                self.query.find_nodes(
                    keyword
                )
            )

            matches.extend(
                nodes
            )

        unique = {}

        for node in matches:

            unique[
                node["id"]
            ] = node

        nodes = list(
            unique.values()
        )

        filtered = []

        for node in nodes:

            label = node.get(
                "label",
                ""
            )

            file_type = node.get(
                "file_type",
                ""
            )

            # Skip noisy rationale nodes
            if file_type == "rationale":
                continue

            # Skip huge text blocks
            if len(label) > 100:
                continue

            filtered.append(
                node
            )

        return filtered[:limit]
