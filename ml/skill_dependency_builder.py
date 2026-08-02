import pickle
import pandas as pd

from config import DATA_PATH, KNOWLEDGE_GRAPH_PATH



print("Loading dataset...")

df = pd.read_csv(DATA_PATH)



print("Loading knowledge graph...")

with open(
    KNOWLEDGE_GRAPH_PATH,
    "rb"
) as f:

    graph = pickle.load(f)



print("Building strict skill dependencies...")



new_edges = 0



# Important technical keywords
# Keep only technical prerequisite relationships

technical_keywords = [

    "Python",
    "Programming",
    "Machine Learning",
    "Deep Learning",
    "Statistics",
    "Mathematics",
    "Algorithms",
    "Data",
    "SQL",
    "Database",
    "Computer",
    "Artificial Intelligence",
    "Neural",
    "Learning",
    "Cloud",
    "Programming Language"

]




def is_technical(skill):

    for word in technical_keywords:

        if word.lower() in skill.lower():

            return True

    return False





for _, row in df.iterrows():



    skills = []

    prerequisites = []



    if isinstance(
        row.get("skills"),
        str
    ):

        skills = [

            s.strip()

            for s in row["skills"].split(",")

        ]



    if isinstance(
        row.get("prerequisites"),
        str
    ):

        prerequisites = [

            p.strip()

            for p in row["prerequisites"].split(",")

        ]



    skills = [

        s for s in skills

        if s in graph.nodes

        and is_technical(s)

    ]



    prerequisites = [

        p for p in prerequisites

        if p in graph.nodes

        and is_technical(p)

    ]




    for prereq in prerequisites:


        for skill in skills:



            if prereq == skill:
                continue



            if not graph.has_edge(
                skill,
                prereq
            ):


                graph.add_edge(

                    skill,

                    prereq,

                    relation="requires",

                    weight=1.0

                )


                new_edges += 1




print("\nSkill dependencies added")

print(
    "New edges:",
    new_edges
)


print(
    "Nodes:",
    graph.number_of_nodes()
)


print(
    "Edges:",
    graph.number_of_edges()
)




with open(
    KNOWLEDGE_GRAPH_PATH,
    "wb"
) as f:

    pickle.dump(
        graph,
        f
    )



print("\nGraph updated")