
class ContextBuilder:

    def build(
        self,
        vector_chunks,
        graph_nodes,
    ):

        context = []

        context.append(
            "VECTOR CONTEXT"
        )

        context.append("=" * 50)

        for score, chunk in vector_chunks:

            context.append(
                f"Score: {score:.4f}"
            )

            context.append(
                chunk.get(
                    "content",
                    "",
                )
            )

            context.append("")

        context.append("")
        context.append(
            "GRAPH CONTEXT"
        )

        context.append("=" * 50)

        for node in graph_nodes:

            context.append(
                node.get(
                    "label",
                    "",
                )
            )

        return "\n".join(context)