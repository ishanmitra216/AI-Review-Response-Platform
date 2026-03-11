from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import review_routes, response_routes, dataset_routes

app = FastAPI(
    title="AI Review Response Platform",
    version="1.0.0"
)

# allow frontend to communicate with API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review_routes.router, prefix="/reviews", tags=["Reviews"])
app.include_router(response_routes.router, prefix="/responses", tags=["Responses"])
# route used for uploading training/analysis datasets
app.include_router(dataset_routes.router, prefix="/datasets", tags=["Datasets"])


@app.get("/")
def root():
    return {"message": "AI Review Response Automation API Running"}