import pickle
import os


class KnowledgeGraphEngine:


    def __init__(self):

        BASE_DIR = os.path.dirname(
            os.path.abspath(__file__)
        )

        GRAPH_PATH = os.path.join(
            BASE_DIR,
            "knowledge_graph.pkl"
        )


        print("Loading knowledge graph...")


        with open(
            GRAPH_PATH,
            "rb"
        ) as f:

            self.graph = pickle.load(f)



    # ------------------------------------
    # Get prerequisite skills for a skill
    # Graph direction:
    #
    # Skill ---> Prerequisite
    #
    # Example:
    #
    # Deep Learning
    #       |
    #       | requires
    #       ↓
    # PyTorch
    #
    # ------------------------------------

    def get_skill_prerequisites(
        self,
        skill
    ):


        if skill not in self.graph:

            return []



        prerequisites = []



        for node in self.graph.successors(skill):


            edge_data = self.graph.get_edge_data(
                skill,
                node
            )



            if (
                edge_data
                and
                edge_data.get("relation")
                ==
                "requires"
            ):

                prerequisites.append(node)



        return prerequisites





    # ------------------------------------
    # Get courses teaching a skill
    #
    # Course ---> Skill
    #
    # ------------------------------------

    def get_courses_for_skill(
        self,
        skill
    ):


        if skill not in self.graph:

            return []



        courses = []



        for node in self.graph.predecessors(skill):


            data = self.graph.nodes[node]


            edge_data = self.graph.get_edge_data(
                node,
                skill
            )



            if (
                data.get("type")
                ==
                "course"

                and

                edge_data.get("relation")
                ==
                "teaches"
            ):

                courses.append(node)



        return courses





    # ------------------------------------
    # Get skills taught by a course
    #
    # Course ---> Skill
    #
    # ------------------------------------

    def get_course_skills(
        self,
        course
    ):


        if course not in self.graph:

            return []



        skills = []



        for node in self.graph.successors(course):


            edge_data = self.graph.get_edge_data(
                course,
                node
            )



            if (
                edge_data
                and
                edge_data.get("relation")
                ==
                "teaches"
            ):

                skills.append(node)



        return skills





    # ------------------------------------
    # Display skill information
    # ------------------------------------

    def show_skill_info(
        self,
        skill
    ):


        print("\nSkill:")
        print(skill)



        print("\nPrerequisites:")


        prerequisites = self.get_skill_prerequisites(
            skill
        )



        if prerequisites:


            for p in prerequisites:

                print("-", p)


        else:

            print("No prerequisites found")





        print("\nCourses teaching this skill:")



        courses = self.get_courses_for_skill(
            skill
        )



        if courses:


            for c in courses:

                print("-", c)


        else:

            print("No courses found")






# ------------------------------------
# Test
# ------------------------------------

if __name__ == "__main__":


    engine = KnowledgeGraphEngine()



    test_skill = "Deep Learning"



    engine.show_skill_info(
        test_skill
    )