# from mentor.graph.graph_service import (
#     GraphService,
# )

# from mentor.graph.graph_query import (
#     GraphQuery,
# )

# GRAPH_PATH = (
#     "data/repositories/langchain/"
#     "graphify-out/graph.json"
# )

# service = GraphService()

# graph = service.load_graph(
#     GRAPH_PATH
# )

# query = GraphQuery(graph)

# nodes = query.find_nodes(
#     "prompt"
# )

# print()
# print("Matches:", len(nodes))
# print()

# # for node in nodes[:10]:
# #     print(node["label"])
# for node in nodes[:5]:
#     print(node)
#     print()

####################################################################
# from mentor.graph.graph_service import GraphService

# GRAPH_PATH = (
#     "data/repositories/langchain/"
#     "graphify-out/graph.json"
# )

# graph_service = GraphService()

# graph = graph_service.load_graph(
#     GRAPH_PATH
# )

# print("\nFIRST NODE\n")
# print(graph["nodes"][0])

# print("\nFIRST LINK\n")
# print(graph["links"][0])


####################################################################
from mentor.graph.graph_service import (
    GraphService,
)


GRAPH_PATH = (
    "data/repositories/langchain/"
    "graphify-out/graph.json"
)


graph_service = GraphService()

graph = graph_service.load_graph(
    GRAPH_PATH
)

stats = graph_service.get_stats(
    graph
)

print(
    "Nodes:",
    stats["nodes"]
)

print(
    "Edges:",
    stats["edges"]
)

print()
