from fastapi import FastAPI

from backend.routes.recommendation import router as recommendation_router


app = FastAPI(
    title="Learning Recommendation System API",
    version="1.0.0",
    description="API for recommending similar learning courses."
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Learning Recommendation System API!"
    }


app.include_router(recommendation_router)