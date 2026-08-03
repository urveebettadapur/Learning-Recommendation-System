import pandas as pd

from graph_engine import KnowledgeGraphEngine
from skill_gap_detector import SkillGapDetector
from config import DATA_PATH



class CourseRankingEngine:


    def __init__(self):

        self.graph_engine = KnowledgeGraphEngine()

        self.skill_detector = SkillGapDetector()

        print("Loading course dataset...")

        self.df = pd.read_csv(DATA_PATH)



    # -------------------------------------------------
    # Get skills taught by a course
    # -------------------------------------------------

    def get_course_skills(
        self,
        course
    ):

        return set(
            self.graph_engine
            .get_course_skills(course)
        )



    # -------------------------------------------------
    # Skill relevance score
    # -------------------------------------------------

    def calculate_skill_score(
        self,
        course,
        required_skills
    ):


        course_skills = (
            self.get_course_skills(course)
        )


        if not course_skills:

            return 0



        overlap = (
            course_skills
            &
            required_skills
        )


        if len(overlap) == 0:

            return 0



        score = (
            len(overlap)
            /
            len(required_skills)
        )


        return min(
            score,
            1.0
        )



    # -------------------------------------------------
    # Difficulty matching
    # -------------------------------------------------

    def difficulty_score(
        self,
        course
    ):


        row = self.df[
            self.df["name"] == course
        ]


        if row.empty:

            return 0.5



        difficulty = (
            row.iloc[0]["difficulty"]
        )


        if difficulty == "Beginner":

            return 1.0


        elif difficulty == "Intermediate":

            return 0.8


        elif difficulty == "Advanced":

            return 0.6


        return 0.5




    # -------------------------------------------------
    # Goal role alignment
    # -------------------------------------------------

    def goal_alignment_score(
        self,
        course,
        target_role=None
    ):


        if target_role is None:

            return 0.5



        row = self.df[
            self.df["name"] == course
        ]


        if row.empty:

            return 0.5



        roles = str(
            row.iloc[0]["goal_role"]
        )


        if target_role.lower() in roles.lower():

            return 1.0


        return 0.3




    # -------------------------------------------------
    # Final ranking score
    # -------------------------------------------------

    def calculate_final_score(
        self,
        course,
        required_skills,
        target_role=None
    ):


        skill_score = (
            self.calculate_skill_score(
                course,
                required_skills
            )
        )


        if skill_score == 0:

            return 0



        difficulty = (
            self.difficulty_score(
                course
            )
        )


        goal_score = (
            self.goal_alignment_score(
                course,
                target_role
            )
        )



        final_score = (

            0.60 * skill_score

            +

            0.20 * difficulty

            +

            0.20 * goal_score

        )



        return round(
            final_score,
            2
        )



    # -------------------------------------------------
    # Rank courses
    # -------------------------------------------------

    def rank_courses(
        self,
        missing_skills,
        target_role=None,
        top_n=10
    ):


        required_skills = set(
            missing_skills
        )



        ranked_courses = []



        for course in self.df["name"]:


            score = (
                self.calculate_final_score(
                    course,
                    required_skills,
                    target_role
                )
            )



            if score > 0:


                ranked_courses.append(

                    {
                        "course": course,
                        "score": score,
                        "difficulty":
                        self.df[
                            self.df["name"] == course
                        ]
                        .iloc[0]["difficulty"]
                    }

                )



        ranked_courses.sort(

            key=lambda x:x["score"],

            reverse=True

        )



        return ranked_courses[:top_n]





# -------------------------------------------------
# TEST
# -------------------------------------------------

if __name__ == "__main__":



    engine = CourseRankingEngine()



    target_skill = "Deep Learning"



    current_skills = [

        "Python Programming",

        "NumPy",

        "Pandas (Python Package)"

    ]



    print("\nGenerating skill gap...\n")



    missing = (

        engine.skill_detector
        .detect_skill_gap(
            current_skills,
            target_skill
        )

    )



    print("==============================")
    print("RANKED COURSE RECOMMENDATIONS")
    print("==============================")



    results = engine.rank_courses(

        missing_skills=missing,

        target_role="AI Engineer",

        top_n=10

    )



    for i, course in enumerate(
        results,
        start=1
    ):


        print(
            f"\n{i}. {course['course']}"
        )


        print(
            "Score:",
            course["score"]
        )


        print(
            "Difficulty:",
            course["difficulty"]
        )