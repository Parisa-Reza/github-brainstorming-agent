from mentor.graph.graph_loader import GraphLoader


class GraphService:

    def __init__(self):
        self.loader = GraphLoader()

    def load_graph(
        self,
        graph_path: str,
    ):
        return self.loader.load(
            graph_path
        )

    def get_stats(
        self,
        graph_data,
    ):

        return {
            "nodes": len(
                graph_data.get(
                    "nodes",
                    []
                )
            ),
            "edges": len(
                graph_data.get(
                    "links",
                    []
                )
            ),
        }