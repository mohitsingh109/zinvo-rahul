from fastapi import FastAPI

from app.routes import api_router

app = FastAPI(title="zinvo-rahul")
app.include_router(api_router)


@app.get("/health")
def health():
    # kafka consumer health check + other stuff
    return {"status": "ok"}
