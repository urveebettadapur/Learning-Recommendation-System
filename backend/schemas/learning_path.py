from pydantic import BaseModel
from typing import List, Dict



class LearningPathRequest(BaseModel):

    goal_role: str

    known_skills: List[str]

    experience: str




class LearningPathResponse(BaseModel):

    missing_skills: List[str]

    recommended_courses: List[str]

    estimated_duration: Dict

    learning_path: List[str]