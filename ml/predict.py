import joblib

from config import (
    TFIDF_PATH,
    COSINE_PATH,
    INDICES_PATH,
    COURSE_DATA_PATH
)


class CourseRecommender:
    """
    Loads trained recommendation artifacts
    and returns similar course recommendations.
    """

    def __init__(self):

        print("Loading trained recommendation model...")

        # Load saved artifacts
        self.tfidf = joblib.load(TFIDF_PATH)
        self.cosine_sim = joblib.load(COSINE_PATH)
        self.indices = joblib.load(INDICES_PATH)
        self.df = joblib.load(COURSE_DATA_PATH)

        print("Recommendation model loaded successfully!")

         # Temporary debugging
        print("\nAvailable Courses:")
        print(self.df["name"].head(10))

    def recommend(self, course_name, top_n=5):
        """
        Recommend the top N similar courses.

        Parameters
        ----------
        course_name : str
            Name of the course selected by the user.

        top_n : int
            Number of recommendations to return.

        Returns
        -------
        list
            List of recommended courses.
        """

        # Check whether the course exists
        if course_name not in self.indices.index:
            raise ValueError(
                f"Course '{course_name}' not found."
            )

        # Get index of selected course
        idx = self.indices[course_name]

        # Get similarity scores
        similarity_scores = list(
            enumerate(self.cosine_sim[idx])
        )

        # Sort by similarity score
        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        # Ignore the first result (same course)
        similarity_scores = similarity_scores[1: top_n + 1]

        recommendations = []

        for course_index, similarity in similarity_scores:

            course = self.df.iloc[course_index]

            recommendations.append(
                {
                    "course_name": course["name"],
                    "category": course["category"],
                    "difficulty": course["difficulty"],
                    "goal_role": course["goal_role"],
                    "estimated_hours": course["estimated_hours"],
                    "skills": course["skills"],
                    "match_percentage": round(
                        similarity * 100,
                        2
                    )
                }
            )

        return recommendations


def main():

    recommender = CourseRecommender()

    print("\n==========================================")
    print(" Course Recommendation System ")
    print("==========================================")

    course_name = input(
        "\nEnter course name: "
    )

    try:

        recommendations = recommender.recommend(
            course_name=course_name,
            top_n=5
        )

        print("\nTop Recommendations\n")

        for i, course in enumerate(
            recommendations,
            start=1
        ):

            print(f"{i}. {course['course_name']}")
            print(f"   Match Score     : {course['match_percentage']}%")
            print(f"   Category        : {course['category']}")
            print(f"   Difficulty      : {course['difficulty']}")
            print(f"   Goal Role       : {course['goal_role']}")
            print(f"   Estimated Hours : {course['estimated_hours']}")
            print(f"   Skills          : {course['skills']}")
            print()

    except ValueError as error:

        print(error)


if __name__ == "__main__":
    main()