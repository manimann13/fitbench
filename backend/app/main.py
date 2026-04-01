from fastapi import FastAPI

app = FastAPI(title="FitBench API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
