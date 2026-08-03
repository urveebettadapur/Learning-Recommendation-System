from graph_engine import KnowledgeGraphEngine
from skill_gap_detector import SkillGapDetector

import networkx as nx


class LearningPathOptimizer:

    def __init__(self):

        self.engine = KnowledgeGraphEngine()
        self.detector = SkillGapDetector()


    # --------------------------------------
    # Build dependency graph
    # --------------------------------------

    def build_learning_graph(
        self,
        missing_skills
    ):

        G = nx.DiGraph()

        visited = set()


        def add_skill(skill):

            if skill in visited:
                return

            visited.add(skill)

            G.add_node(skill)

            prerequisites = (
                self.engine.get_skill_prerequisites(skill)
            )

            for prereq in prerequisites:

                if prereq in missing_skills:

                    G.add_node(prereq)

                    # prerequisite -> skill
                    G.add_edge(
                        prereq,
                        skill
                    )

                    add_skill(prereq)


        for skill in missing_skills:

            add_skill(skill)

        return G


    # --------------------------------------
    # Optimize learning path
    # --------------------------------------

    def optimize_learning_path(
        self,
        current_skills,
        target_skill
    ):

        missing_skills = (
            self.detector.detect_skill_gap(
                current_skills,
                target_skill
            )
        )

        if not missing_skills:

            return []


        learning_graph = self.build_learning_graph(
            missing_skills
        )


        try:

            ordered_path = list(
                nx.topological_sort(
                    learning_graph
                )
            )

        except nx.NetworkXUnfeasible:

            # fallback if graph contains a cycle

            ordered_path = sorted(
                list(missing_skills)
            )

        return ordered_path


# --------------------------------------
# TEST
# --------------------------------------

if __name__ == "__main__":

    optimizer = LearningPathOptimizer()


    current_skills = [

        "Python Programming",
        "NumPy",
        "Pandas (Python Package)"

    ]


    target_skill = "Deep Learning"


    learning_path = optimizer.optimize_learning_path(

        current_skills,

        target_skill

    )


    print("\n==============================")

    print("PERSONALIZED LEARNING PATH")

    print("==============================\n")


    if learning_path:

        for i, skill in enumerate(

            learning_path,

            start=1

        ):

            print(f"{i}. {skill}")

    else:

        print("No learning path required.")