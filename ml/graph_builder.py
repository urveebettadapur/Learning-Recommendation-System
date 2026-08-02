import pandas as pd
import networkx as nx
import pickle
import os

from config import DATA_PATH


def build_knowledge_graph():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

    print("Dataset loaded:", df.shape)


    # Create graph
    G = nx.DiGraph()


    for _, row in df.iterrows():

        # ==========================
        # Course Node
        # ==========================

        course = row["name"]

        G.add_node(
            course,
            type="course",
            difficulty=row["difficulty"],
            category=row["category"]
        )


        # ==========================
        # Course -> Skill
        # ==========================

        skills = str(row["skills"]).split(",")

        for skill in skills:

            skill = skill.strip()

            if skill and skill.lower() != "nan":

                G.add_node(
                    skill,
                    type="skill"
                )

                G.add_edge(
                    course,
                    skill,
                    relation="teaches"
                )


        # ==========================
        # Prerequisite -> Course
        # ==========================

        prerequisites = str(row["prerequisites"]).split(",")

        for prereq in prerequisites:

            prereq = prereq.strip()

            if prereq and prereq.lower() != "nan":

                G.add_node(
                    prereq,
                    type="skill"
                )

                G.add_edge(
                    prereq,
                    course,
                    relation="required_before"
                )


    print("\nGraph Created Successfully")

    print(
        "Total Nodes:",
        G.number_of_nodes()
    )

    print(
        "Total Edges:",
        G.number_of_edges()
    )


    # ==========================
    # Save graph inside ml folder
    # ==========================

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    GRAPH_PATH = os.path.join(
        BASE_DIR,
        "knowledge_graph.pkl"
    )


    with open(
        GRAPH_PATH,
        "wb"
    ) as f:

        pickle.dump(
            G,
            f
        )


    print(
        "\nKnowledge graph saved at:"
    )

    print(
        GRAPH_PATH
    )


if __name__ == "__main__":

    build_knowledge_graph()