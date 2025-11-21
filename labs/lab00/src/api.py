from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.medical_assistant import MedicalAssistant

app = FastAPI(title="Medical Virtual Assistant API")
agent = MedicalAssistant()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_agent(request: QueryRequest):
    response = agent.process_query(request.query)
    return {"response": response}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
