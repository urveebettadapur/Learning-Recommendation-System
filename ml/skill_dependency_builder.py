import pickle
import pandas as pd
from pathlib import Path

from config import DATA_PATH, KNOWLEDGE_GRAPH_PATH


print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print("Loading knowledge graph...")

with open(KNOWLEDGE_GRAPH_PATH, "rb") as f:
    graph = pickle.load(f)


print("Building strict skill dependencies...")


new_edges = 0


for _, row in df.iterrows():

    # Skills taught by the course
    skills = []

    if isinstance(row.get("skills"), str):
        skills.extend(
            [s.strip() for s in row["skills"].split(",")]
        )


    # Course prerequisites
    prerequisites = []

    if isinstance(row.get("prerequisites"), str):
        prerequisites.extend(
            [p.strip() for p in row["prerequisites"].split(",")]
        )


    # Remove empty values

    skills = [
        s for s in skills
        if s and s in graph.nodes
    ]

    prerequisites = [
        p for p in prerequisites
        if p and p in graph.nodes
    ]


    # Create prerequisite relationships

    for prereq in prerequisites:

        for skill in skills:

            if prereq != skill:

                if not graph.has_edge(prereq, skill):

                    graph.add_edge(
                        skill,
                        prereq,
                        relation="requires",
                        weight= 1.0
                    )

                    new_edges += 1



print("\nSkill dependencies added")

print("New edges:", new_edges)

print("Nodes:", graph.number_of_nodes())

print("Edges:", graph.number_of_edges())



with open(KNOWLEDGE_GRAPH_PATH, "wb") as f:
    pickle.dump(graph, f)


print("\nGraph updated")