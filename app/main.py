from fastapi import FastAPI

from app.routes import api_router

app = FastAPI(title="zinvo-rahul")
app.include_router(api_router)


@app.get("/health")
def health():
    return {"status": "ok"}
