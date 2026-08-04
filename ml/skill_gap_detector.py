from ml.graph_engine import KnowledgeGraphEngine


class SkillGapDetector:


    def __init__(self):

        self.engine = KnowledgeGraphEngine()



    # --------------------------------------
    # Recursive prerequisite search
    # with depth control
    # --------------------------------------

    def get_required_skills(
        self,
        target_skill,
        max_depth=1
    ):

        required = set()

        visited = set()



        def traverse(skill, depth):


            if depth > max_depth:
                return


            if skill in visited:
                return


            visited.add(skill)



            prerequisites = (
                self.engine
                .get_skill_prerequisites(skill)
            )



            for prereq in prerequisites:


                required.add(prereq)


                traverse(
                    prereq,
                    depth + 1
                )



        traverse(
            target_skill,
            0
        )


        return required




    # --------------------------------------
    # Remove noisy prerequisite relationships
    # --------------------------------------

    def filter_skill_noise(
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

            "Data Architecture"

        }



        filtered = (

            set(skills)
            -
            noisy_skills

        )


        return filtered




    # --------------------------------------
    # Detect skill gap
    # --------------------------------------

    def detect_skill_gap(
        self,
        current_skills,
        target_skill
    ):


        required_skills = (

            self.get_required_skills(
                target_skill
            )

        )



        # Remove irrelevant graph noise

        required_skills = (

            self.filter_skill_noise(
                required_skills
            )

        )



        current_skills = set(
            current_skills
        )



        missing = (

            required_skills
            -
            current_skills

        )



        return missing




    # --------------------------------------
    # Generate learning path
    # --------------------------------------

    def generate_learning_path(
        self,
        missing_skills
    ):


        path = []


        for skill in missing_skills:


            prerequisites = (

                self.engine
                .get_skill_prerequisites(skill)

            )


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
        missing_skills
    ):


        courses = set()



        for skill in missing_skills:


            results = (

                self.engine
                .get_courses_for_skill(skill)

            )


            for course in results:

                courses.add(course)



        return courses





# --------------------------------------
# TEST
# --------------------------------------

if __name__ == "__main__":


    detector = SkillGapDetector()



    target_skill = "Deep Learning"



    current_skills = [

        "Python Programming",
        "NumPy",
        "Pandas (Python Package)"

    ]



    print("\n==============================")
    print("TARGET SKILL:")
    print(target_skill)



    print("\nCURRENT SKILLS:")

    for skill in current_skills:

        print("-", skill)



    missing = detector.detect_skill_gap(
        current_skills,
        target_skill
    )



    print("\nMISSING SKILLS:")



    if missing:

        for skill in sorted(missing):

            print("-", skill)

    else:

        print("No missing skills")




    print("\nLEARNING PATH:")



    path = detector.generate_learning_path(
        missing
    )



    for item in path:


        print(
            "\n",
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


    for course in list(courses)[:10]:

        print("-", course)