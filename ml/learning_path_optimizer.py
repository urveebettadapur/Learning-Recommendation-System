from ml.graph_engine import KnowledgeGraphEngine
from ml.skill_gap_detector import SkillGapDetector
from ml.roadmap_enhancer import RoadmapEnhancer



class LearningPathOptimizer:


    def __init__(self):

        self.graph_engine = KnowledgeGraphEngine()

        self.skill_detector = SkillGapDetector()

        self.roadmap_enhancer = RoadmapEnhancer()



    # ----------------------------------------------------
    # Expand dependencies recursively
    # ----------------------------------------------------

    def expand_dependencies(
        self,
        skills,
        max_depth=2
    ):


        expanded = set()



        def traverse(
            skill,
            depth
        ):


            if depth > max_depth:

                return



            if skill in expanded:

                return



            expanded.add(skill)



            prerequisites = (

                self.graph_engine
                .get_skill_prerequisites(skill)

            )



            for prereq in prerequisites:


                traverse(

                    prereq,

                    depth + 1

                )



        for skill in skills:


            traverse(

                skill,

                0

            )



        return expanded




    # ----------------------------------------------------
    # Remove unrelated graph noise
    # ----------------------------------------------------

    def filter_noise(
        self,
        skills
    ):


        noisy_skills = {


            "Databricks",

            "Cloud Solutions",

            "Cloud Security",

            "Amazon CloudWatch",

            "Human Computer Interaction",

            "Data Lakes",

            "Data Architecture",

            "Computer Vision",

            "Data Security",

            "Data Ethics",

            "Data Storage Technologies"


        }



        return (

            set(skills)

            -

            noisy_skills

        )




    # ----------------------------------------------------
    # Topological sorting
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
    # Generate learning path
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



        print("\nRaw Missing Skills:")



        for skill in sorted(missing_skills):

            print("-", skill)




        complete_skill_set = (

            self.expand_dependencies(

                missing_skills | {target_skill}

            )

        )



        complete_skill_set = (

            self.filter_noise(

                complete_skill_set

            )

        )



        complete_skill_set -= set(

            current_skills

        )



        learning_path = (

            self.topological_sort(

                complete_skill_set

            )

        )



        return learning_path




    # ----------------------------------------------------
    # Compatibility wrapper
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

        "Machine Learning",

        "Artificial Neural Networks",

        "PyTorch (Machine Learning Library)"
    ]

    print("TEST PROFILE:")
    print(current_skills)

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




    completion_time = (

        optimizer
        .roadmap_enhancer
        .estimate_completion_time(

            roadmap

        )

    )



    print("\n")

    print("==============================")

    print("ESTIMATED COMPLETION TIME")

    print("==============================")



    print(

        completion_time

    )




    difficulty = (

        optimizer
        .roadmap_enhancer
        .generate_difficulty_progression(

            roadmap

        )

    )



    print("\n")

    print("==============================")

    print("DIFFICULTY PROGRESSION")

    print("==============================")



    for item in difficulty:


        print(

            f"{item['skill']} → {item['difficulty']}"

        )