import pandas as pd
import pickle
import os

from config import DATA_PATH



def clean_skills(value):

    if pd.isna(value):
        return []

    return [
        x.strip()
        for x in str(value)
        .replace(";", ",")
        .split(",")
        if x.strip()
    ]



def build_skill_dependencies():


    print("Loading dataset...")


    df = pd.read_csv(DATA_PATH)



    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )


    GRAPH_PATH = os.path.join(
        BASE_DIR,
        "knowledge_graph.pkl"
    )



    print("Loading knowledge graph...")


    with open(
        GRAPH_PATH,
        "rb"
    ) as f:

        G = pickle.load(f)



    print("Building skill dependencies...")



    new_edges = 0



    for _, row in df.iterrows():


        prerequisites = clean_skills(
            row["prerequisites"]
        )


        taught_skills = clean_skills(
            row["core_skills"]
        )



        # prerequisite skill
        #        |
        #        |
        #        v
        #      course
        #        |
        #        |
        #        v
        #     taught skill


        for prereq in prerequisites:


            for skill in taught_skills:



                if prereq == skill:
                    continue



                if (
                    G.has_node(prereq)
                    and
                    G.has_node(skill)
                ):


                    if not G.has_edge(
                        prereq,
                        skill
                    ):


                        G.add_edge(
                            prereq,
                            skill,
                            relation="requires"
                        )


                        new_edges += 1




    print("\nSkill dependencies added")

    print(
        "New dependency edges:",
        new_edges
    )


    print(
        "Nodes:",
        G.number_of_nodes()
    )


    print(
        "Edges:",
        G.number_of_edges()
    )



    with open(
        GRAPH_PATH,
        "wb"
    ) as f:

        pickle.dump(
            G,
            f
        )


    print("\nKnowledge graph updated")




if __name__ == "__main__":

    build_skill_dependencies()