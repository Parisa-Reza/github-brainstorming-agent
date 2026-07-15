import json
from pathlib import Path


class GraphLoader:

    def load(self, graph_path: str):

        graph_file = Path(graph_path)

        with open(
            graph_file,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)