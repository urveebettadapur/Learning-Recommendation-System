import joblib

from difflib import get_close_matches

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

        self.tfidf = joblib.load(TFIDF_PATH)
        self.cosine_sim = joblib.load(COSINE_PATH)
        self.indices = joblib.load(INDICES_PATH)
        self.df = joblib.load(COURSE_DATA_PATH)

        print("Recommendation model loaded successfully!")

    def find_course(self, user_input):
        """
        Finds the correct course name using:
        1. Case-insensitive exact match
        2. Partial match
        3. Close match suggestions
        """

        user_input = user_input.strip().lower()

        # -----------------------------
        # Case-insensitive lookup
        # -----------------------------

        course_lookup = {
            name.lower(): name
            for name in self.indices.index
        }

        if user_input in course_lookup:
            return course_lookup[user_input]

        # -----------------------------
        # Partial matches
        # -----------------------------

        partial_matches = [
            name
            for name in self.indices.index
            if user_input in name.lower()
        ]

        if len(partial_matches) == 1:
            return partial_matches[0]

        elif len(partial_matches) > 1:

            print("\nMultiple matching courses found:\n")

            for i, course in enumerate(
                partial_matches,
                start=1
            ):
                print(f"{i}. {course}")

            while True:

                try:

                    choice = int(
                        input("\nChoose a course number: ")
                    )

                    if 1 <= choice <= len(partial_matches):
                        return partial_matches[choice - 1]

                    print("Invalid choice.")

                except ValueError:

                    print("Please enter a valid number.")

        # -----------------------------
        # Close match suggestions
        # -----------------------------

        suggestions = get_close_matches(
            user_input,
            self.indices.index,
            n=5,
            cutoff=0.4
        )

        if suggestions:

            print("\nDid you mean:\n")

            for suggestion in suggestions:
                print(f"- {suggestion}")

        raise ValueError(
            f"\nCourse '{user_input}' not found."
        )

    def recommend(self, course_name, top_n=5):
        """
        Recommend the top N similar courses.
        """

        course_name = self.find_course(course_name)
        print(f"\nUsing course: {course_name}")

        idx = self.indices[course_name]

        similarity_scores = list(
            enumerate(
                self.cosine_sim[idx]
            )
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        similarity_scores = similarity_scores[
            1: top_n + 1
        ]

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