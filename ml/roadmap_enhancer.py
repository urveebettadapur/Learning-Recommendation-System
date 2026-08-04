from graph_engine import KnowledgeGraphEngine


class RoadmapEnhancer:


    def __init__(self):

        self.engine = KnowledgeGraphEngine()



    # ----------------------------------------
    # Calculate estimated completion time
    # ----------------------------------------

    def estimate_completion_time(
        self,
        learning_path
    ):

        total_hours = 0


        for skill in learning_path:

            courses = (
                self.engine
                .get_courses_for_skill(skill)
            )


            # temporary estimate
            # until course metadata is connected

            total_hours += len(courses) * 5


        weeks = round(
            total_hours / 5
        )


        return {
            "total_hours": total_hours,
            "estimated_weeks": weeks
        }



    # ----------------------------------------
    # Difficulty progression
    # ----------------------------------------

    def generate_difficulty_progression(
        self,
        learning_path
    ):


        progression = []


        total = len(learning_path)


        for index, skill in enumerate(
            learning_path
        ):


            if index < total * 0.4:

                level = "Beginner"


            elif index < total * 0.75:

                level = "Intermediate"


            else:

                level = "Advanced"



            progression.append(
                {
                    "skill": skill,
                    "difficulty": level
                }
            )


        return progression