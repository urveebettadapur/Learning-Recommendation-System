from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    course_name: str
    top_n: int = 5


class RecommendationResponse(BaseModel):
    course_name: str
    category: str
    difficulty: str
    goal_role: str
    estimated_hours: int
    skills: str
    match_percentage: float