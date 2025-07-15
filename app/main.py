from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.agent import ask_question  

app = FastAPI()

@app.post("/ask")
async def ask(question: dict):
    try:
        result = await ask_question(question["question"])
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}