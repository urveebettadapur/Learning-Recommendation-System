from graph_engine import KnowledgeGraphEngine


class SkillGapDetector:

    def __init__(self):

        self.engine = KnowledgeGraphEngine()



    # --------------------------------
    # Find prerequisite skills required
    # for target skill
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
    # Detect user's missing skills
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
    # Recommend courses for missing
    # skills
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




if __name__ == "__main__":


    detector = SkillGapDetector()



    # Example user profile

    current_skills = [

        "Python Programming",
        "NumPy",
        "Pandas (Python Package)"

    ]


    target_skill = "Deep Learning"



    print("\nTarget Skill:")
    print(target_skill)



    print("\nCurrent Skills:")

    for skill in current_skills:

        print("-", skill)



    missing = detector.detect_skill_gap(
        current_skills,
        target_skill
    )



    print("\nMissing Skills:")


    if missing:

        for skill in sorted(missing):

            print("-", skill)

    else:

        print("No missing skills")



    courses = detector.recommend_courses(
        missing
    )



    print("\nRecommended Courses:")


    if courses:

        for course in list(courses)[:10]:

            print("-", course)

    else:

        print("No courses found")