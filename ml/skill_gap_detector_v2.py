import os
import pickle


class SkillGapDetector:


    def __init__(self):

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

            self.graph = pickle.load(f)



    # --------------------------------------
    # Find all prerequisites recursively
    # --------------------------------------

    def get_all_prerequisites(
        self,
        skill,
        visited=None
    ):


        if visited is None:
            visited = set()



        if skill in visited:
            return visited



        visited.add(skill)



        if skill not in self.graph:
            return visited



        for node in self.graph.predecessors(skill):


            edge = self.graph.get_edge_data(
                node,
                skill
            )


            if (
                edge
                and
                edge.get("relation")
                ==
                "requires"
            ):

                self.get_all_prerequisites(
                    node,
                    visited
                )



        return visited




    # --------------------------------------
    # Remove skills user already knows
    # --------------------------------------

    def detect_gap(
        self,
        target_skill,
        current_skills
    ):


        required_skills = self.get_all_prerequisites(
            target_skill
        )


        required_skills.add(
            target_skill
        )


        missing = (
            required_skills
            -
            set(current_skills)
        )


        return missing




    # --------------------------------------
    # Generate ordered learning path
    # --------------------------------------

    def generate_learning_path(
        self,
        missing_skills
    ):


        path = []



        for skill in missing_skills:


            prerequisites = []


            for node in self.graph.predecessors(skill):


                edge = self.graph.get_edge_data(
                    node,
                    skill
                )


                if (
                    edge
                    and
                    edge.get("relation")
                    ==
                    "requires"
                ):

                    prerequisites.append(node)



            path.append(
                {
                    "skill": skill,
                    "prerequisites": prerequisites
                }
            )



        return path




    # --------------------------------------
    # Recommend courses
    # --------------------------------------

    def recommend_courses(
        self,
        skills
    ):


        courses = []


        for skill in skills:


            if skill not in self.graph:
                continue



            for node in self.graph.predecessors(skill):


                data = self.graph.nodes[node]


                edge = self.graph.get_edge_data(
                    node,
                    skill
                )


                if (
                    data.get("type")
                    ==
                    "course"
                    and
                    edge.get("relation")
                    ==
                    "teaches"
                ):

                    courses.append(node)



        return list(
            dict.fromkeys(courses)
        )





# --------------------------------------
# TEST
# --------------------------------------

if __name__ == "__main__":


    detector = SkillGapDetector()



    target = "Deep Learning"



    current = [
        "Python Programming",
        "NumPy",
        "Pandas (Python Package)"
    ]



    print("\n==============================")
    print("TARGET SKILL:")
    print(target)



    print("\nCURRENT SKILLS:")

    for skill in current:
        print("-", skill)



    missing = detector.detect_gap(
        target,
        current
    )



    print("\nMISSING SKILLS:")

    for skill in missing:
        print("-", skill)



    print("\nLEARNING PATH:")

    path = detector.generate_learning_path(
        missing
    )


    for item in path:

        print(
            "\nSkill:",
            item["skill"]
        )


        print(
            "Prerequisites:",
            item["prerequisites"]
        )



    print("\nRECOMMENDED COURSES:")


    courses = detector.recommend_courses(
        missing
    )


    for course in courses[:10]:

        print(
            "-",
            course
        )