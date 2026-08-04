from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.recommendation import router as recommendation_router
from backend.routes.learning_path import router as learning_path_router



app = FastAPI(

    title="Learning Recommendation System API",

    version="1.0.0",

    description="API for course recommendation and adaptive learning path optimization."

)



# Allow React frontend to communicate with FastAPI backend

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173"

    ],

    allow_credentials=True,

    allow_methods=[

        "*"

    ],

    allow_headers=[

        "*"

    ]

)



@app.get("/")
def home():

    return {

        "message": "Welcome to the Learning Recommendation System API!"

    }



@app.get("/health")
def health():

    return {

        "status": "ok"

    }



# Existing course recommendation API

app.include_router(

    recommendation_router

)



# Adaptive learning path API

app.include_router(

    learning_path_router

)