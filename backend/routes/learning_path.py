from fastapi import APIRouter

from backend.schemas.learning_path import (
    LearningPathRequest,
    LearningPathResponse
)

from backend.services.learning_path_service import (
    LearningPathService
)



router = APIRouter()



service = LearningPathService()



@router.post(
    "/recommend-learning-path",
    response_model=LearningPathResponse
)
def recommend_learning_path(
    request: LearningPathRequest
):


    result = service.generate_learning_path(

        goal_role=request.goal_role,

        known_skills=request.known_skills,

        experience=request.experience

    )


    return result