from graph_engine import KnowledgeGraphEngine


class SkillGapDetector:

    def __init__(self):

        self.engine = KnowledgeGraphEngine()



    # --------------------------------
    # Recursively find all prerequisite
    # skills required for target skill
    # --------------------------------

    def get_required_skills(
        self,
        target_skill
    ):

        required_skills = set()

        visited = set()


        def traverse(skill):

            if skill in visited:
                return

            visited.add(skill)


            prerequisites = self.engine.get_skill_prerequisites(
                skill
            )


            for prereq in prerequisites:

                required_skills.add(
                    prereq
                )

                # recursively find deeper prerequisites

                traverse(prereq)



        traverse(target_skill)


        return required_skills



    # --------------------------------
    # Detect missing skills based on
    # user's current knowledge
    # --------------------------------

    def detect_skill_gap(
        self,
        current_skills,
        target_skill
    ):


        required_skills = self.get_required_skills(
            target_skill
        )


        current_skills = set(
            current_skills
        )


        missing_skills = (
            required_skills
            -
            current_skills
        )


        return missing_skills



    # --------------------------------
    # Generate ordered learning path
    # based on prerequisite hierarchy
    # --------------------------------

    def generate_learning_path(
        self,
        missing_skills
    ):

        learning_path = []


        visited = set()


        def add_skill(skill):

            if skill in visited:
                return

            visited.add(skill)


            prerequisites = self.engine.get_skill_prerequisites(
                skill
            )


            for prereq in prerequisites:

                if prereq in missing_skills:

                    add_skill(prereq)



            learning_path.append(skill)



        for skill in missing_skills:

            add_skill(skill)



        return learning_path



    # --------------------------------
    # Recommend courses that teach
    # missing skills
    # --------------------------------

    def recommend_courses(
        self,
        missing_skills
    ):


        recommended_courses = set()



        for skill in missing_skills:


            courses = self.engine.get_courses_for_skill(
                skill
            )


            for course in courses:

                recommended_courses.add(
                    course
                )



        return recommended_courses





# --------------------------------
# TEST
# --------------------------------

if __name__ == "__main__":


    detector = SkillGapDetector()



    current_skills = [

        "Python Programming",
        "NumPy",
        "Pandas (Python Package)"

    ]



    target_skill = "Deep Learning"



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


    for index, skill in enumerate(path, start=1):

        print(
            f"{index}. {skill}"
        )



    print("\nRECOMMENDED COURSES:")

    courses = detector.recommend_courses(
        missing
    )



    if courses:

        for course in list(courses)[:10]:

            print("-", course)

    else:

        print("No courses found")