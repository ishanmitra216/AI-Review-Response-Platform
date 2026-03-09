from fastapi import FastAPI
from app.api import review_routes, response_routes

app = FastAPI(
    title="AI Review Response Platform",
    version="1.0.0"
)

app.include_router(review_routes.router, prefix="/reviews", tags=["Reviews"])
app.include_router(response_routes.router, prefix="/responses", tags=["Responses"])


@app.get("/")
def root():
    return {"message": "AI Review Response Automation API Running"}