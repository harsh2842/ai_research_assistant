from fastapi import FastAPI

app = FastAPI(
    title="AI Research Agent API",
    version="1.0.0",
)


# =========================================================
# HEALTH
# =========================================================

@app.get("/")
def root():
    return {
        "message":
            "AI Research Agent API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
