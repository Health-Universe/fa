from fastapi import FastAPI

app = FastAPI()

@app.get("{full_path:path}")
async def root(full_path: str):
    return {"message": "Hello World"}
