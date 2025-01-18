from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
import httpx

app = FastAPI()


class AnalyzePRRequest(BaseModel):
    repo_url: str
    pr_number: int
    git_token: Optional[str] = None


@app.post("/start_task")
async def start_task_endpoint(task_request: AnalyzePRRequest):
    data = {
        "repo_url": task_request.repo_url,
        "pr_number": task_request.pr_number,
        "git_token": task_request.git_token
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:8001/start_task/",
            data=data
        )
        return response.json()
    
    return {"task_id": "123", "status": "Task started"}


# http://127.0.0.1:8001/task_status/{task_id}
@app.get("/task_status/{task_id}/")
async def task_status_endpoint(task_id: str):
    async with httpx.AsyncClient() as client:
        # Correcting the URL formatting
        response = await client.get(
            f"http://127.0.0.1:8001/task_status/{task_id}/" 
        )
        return response.json()
    return {"message": "something went wrong"}
