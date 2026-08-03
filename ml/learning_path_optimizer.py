from graph_engine import KnowledgeGraphEngine
from skill_gap_detector import SkillGapDetector


class LearningPathOptimizer:


    def __init__(self):

        self.graph_engine = KnowledgeGraphEngine()

        self.skill_detector = SkillGapDetector()



    # ----------------------------------------------------
    # Expand missing skills with prerequisites recursively
    # ----------------------------------------------------

    def expand_dependencies(
        self,
        skills
    ):

        expanded = set()

        visited = set()



        def traverse(skill):

            if skill in visited:
                return


            visited.add(skill)

            expanded.add(skill)



            prerequisites = (
                self.graph_engine
                .get_skill_prerequisites(skill)
            )



            for prereq in prerequisites:

                traverse(prereq)



        for skill in skills:

            traverse(skill)



        return expanded




    # ----------------------------------------------------
    # Topological sorting
    # Ensures prerequisites appear before skills
    # ----------------------------------------------------

    def topological_sort(
        self,
        skills
    ):

        ordered = []

        visited = set()



        def visit(skill):

            if skill in visited:
                return


            visited.add(skill)



            prerequisites = (
                self.graph_engine
                .get_skill_prerequisites(skill)
            )



            for prereq in prerequisites:

                if prereq in skills:

                    visit(prereq)



            ordered.append(skill)



        for skill in skills:

            visit(skill)



        return ordered




    # ----------------------------------------------------
    # Generate optimized learning path
    # ----------------------------------------------------

    def generate_learning_path(
        self,
        current_skills,
        target_skill
    ):


        print("\nDetecting skill gaps...")



        missing_skills = (

            self.skill_detector
            .detect_skill_gap(

                current_skills,

                target_skill

            )

        )



        print(
            "Missing skills:",
            len(missing_skills)
        )



        # Expand hidden prerequisites

        complete_skill_set = (

            self.expand_dependencies(

                missing_skills

            )

        )



        # Remove already mastered skills

        complete_skill_set -= set(
            current_skills
        )



        # Order learning sequence

        learning_path = (

            self.topological_sort(

                complete_skill_set

            )

        )



        return learning_path




    # ----------------------------------------------------
    # Compatibility wrapper
    #
    # Required by recommendation_engine.py
    #
    # ----------------------------------------------------

    def optimize_learning_path(
        self,
        current_skills,
        target_skill
    ):


        return self.generate_learning_path(
            current_skills,
            target_skill
        )





# ----------------------------------------------------
# TEST
# ----------------------------------------------------

if __name__ == "__main__":


    optimizer = LearningPathOptimizer()



    target_skill = "Deep Learning"



    current_skills = [

        "Python Programming",

        "NumPy",

        "Pandas (Python Package)"

    ]



    roadmap = (

        optimizer
        .generate_learning_path(

            current_skills,

            target_skill

        )

    )



    print("\n")

    print("==============================")

    print("PERSONALIZED LEARNING PATH")

    print("==============================")



    for index, skill in enumerate(
        roadmap,
        start=1
    ):


        print(
            f"{index}. {skill}"
        )