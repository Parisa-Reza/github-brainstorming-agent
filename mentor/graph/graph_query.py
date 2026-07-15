class GraphQuery:

    def __init__(self, graph_data):
        self.graph = graph_data

    def find_nodes(
        self,
        query: str,
    ):

        query = query.lower()

        matches = []

        # for node in self.graph["nodes"]:
        for node in self.graph.get("nodes", []):

            label = node.get(
                "label",
                "",
            ).lower()

            if query in label:
                matches.append(node)

        return matches

    def related_nodes(
        self,
        node_id: str,
    ):

        related = []

        # for link in self.graph["links"]:
        for link in self.graph.get("links", []):

            if link["source"] == node_id:
                related.append(link)

            elif link["target"] == node_id:
                related.append(link)

        return related