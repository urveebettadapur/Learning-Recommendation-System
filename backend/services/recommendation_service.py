from ml.predict import CourseRecommender


# Load the recommendation model once when the server starts
recommender = CourseRecommender()


def get_recommendations(course_name: str, top_n: int = 5):
    return recommender.recommend(
        course_name=course_name,
        top_n=top_n
    )