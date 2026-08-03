from graph_engine import KnowledgeGraphEngine
from learning_path_optimizer import LearningPathOptimizer


class RecommendationEngine:


    def __init__(self):

        self.engine = KnowledgeGraphEngine()

        self.optimizer = LearningPathOptimizer()



    # --------------------------------------
    # Recommend courses for a skill
    # --------------------------------------

    def recommend_courses_for_skill(
        self,
        skill
    ):


        courses = (

            self.engine
            .get_courses_for_skill(skill)

        )


        return courses



    # --------------------------------------
    # Generate complete learning roadmap
    # --------------------------------------

    def generate_recommendation(
        self,
        current_skills,
        target_skill
    ):


        learning_path = (

            self.optimizer
            .optimize_learning_path(

                current_skills,

                target_skill

            )

        )



        roadmap = []



        for skill in learning_path:


            courses = (

                self.recommend_courses_for_skill(
                    skill
                )

            )


            roadmap.append(

                {

                    "skill": skill,

                    "recommended_courses": courses[:5]

                }

            )



        return roadmap




# --------------------------------------
# TEST
# --------------------------------------

if __name__ == "__main__":



    recommender = RecommendationEngine()



    current_skills = [

        "Python Programming",

        "NumPy",

        "Pandas (Python Package)"

    ]



    target_skill = "Deep Learning"



    recommendations = (

        recommender
        .generate_recommendation(

            current_skills,

            target_skill

        )

    )



    print("\n==============================")

    print("PERSONALIZED COURSE ROADMAP")

    print("==============================\n")



    for index, item in enumerate(

        recommendations,

        start=1

    ):


        print(

            f"{index}. {item['skill']}"

        )


        print(
            "Courses:"
        )


        if item["recommended_courses"]:


            for course in item["recommended_courses"]:

                print(
                    " -",
                    course
                )

        else:

            print(
                " No courses found"
            )


        print()