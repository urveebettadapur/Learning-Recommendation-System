import pickle
import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


PATH = os.path.join(
    BASE_DIR,
    "knowledge_graph.pkl"
)


with open(PATH, "rb") as f:
    G = pickle.load(f)


skill = "Deep Learning"


print("Node exists:")
print(skill in G)


print("\nNode data:")
print(G.nodes[skill])


print("\nIncoming edges:")
for u, v, data in G.in_edges(
    skill,
    data=True
):
    print(u, "---->", v, data)


print("\nOutgoing edges:")
for u, v, data in G.out_edges(
    skill,
    data=True
):
    print(u, "---->", v, data)