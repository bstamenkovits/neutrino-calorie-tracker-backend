import uvicorn
from fastapi import FastAPI

from api import auth, meals

app = FastAPI()
app.include_router(auth.router)
app.include_router(meals.router)


@app.get("/status")
def root():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
