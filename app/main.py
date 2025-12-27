from fastapi import FastAPI

app = FastAPI(
    title="Documents API",
    description="API REST para gestão de documentos usando FastAPI e AWS",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
