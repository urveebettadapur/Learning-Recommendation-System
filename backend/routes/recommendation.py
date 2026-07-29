from fastapi import APIRouter

from backend.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)

from backend.services.recommendation_service import (
    get_recommendations
)


router = APIRouter()


@router.post(
    "/recommend",
    response_model=list[RecommendationResponse]
)
def recommend(request: RecommendationRequest):
    """
    Generate course recommendations.
    """

    recommendations = get_recommendations(
        course_name=request.course_name,
        top_n=request.top_n
    )

    return recommendations