from fastapi import FastAPI
from pmla.api import router

app = FastAPI(title="PMLA System API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
