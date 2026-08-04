from ml.learning_path_optimizer import LearningPathOptimizer
from ml.graph_engine import KnowledgeGraphEngine



class LearningPathService:


    def __init__(self):

        self.optimizer = LearningPathOptimizer()

        self.graph_engine = KnowledgeGraphEngine()



    # ----------------------------------------------------
    # Generate personalized learning roadmap
    # ----------------------------------------------------

    def generate_learning_path(
        self,
        goal_role,
        known_skills,
        experience
    ):


        # Map career roles to target skills

        role_mapping = {


            "ML Engineer": "Deep Learning",

            "AI Engineer": "Artificial Intelligence",

            "Data Scientist": "Machine Learning",

            "Data Analyst": "Data Analysis"

        }



        target_skill = role_mapping.get(

            goal_role,

            goal_role

        )



        # Generate learning path

        learning_path = (

            self.optimizer
            .generate_learning_path(

                known_skills,

                target_skill

            )

        )



        # ------------------------------------------------
        # Recommend courses for roadmap skills
        # ------------------------------------------------

        recommended_courses = set()



        for skill in learning_path:


            courses = (

                self.graph_engine
                .get_courses_for_skill(skill)

            )


            for course in courses:

                recommended_courses.add(course)



        # ------------------------------------------------
        # Estimate duration
        # ------------------------------------------------

        estimated_duration = (

            self.optimizer
            .roadmap_enhancer
            .estimate_completion_time(

                learning_path

            )

        )



        # ------------------------------------------------
        # Return API response
        # ------------------------------------------------

        return {


            "missing_skills": learning_path,


            "recommended_courses": list(
                recommended_courses
            )[:10],


            "estimated_duration": estimated_duration,


            "learning_path": learning_path

        }