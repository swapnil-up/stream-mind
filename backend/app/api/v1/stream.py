from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai import stream_ai_response
from sse_starlette.sse import EventSourceResponse

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/stream")
async def stream(request: PromptRequest):
    async def event_generator():
        async for token in stream_ai_response(request.prompt):
            yield {"data": token}
    
    return EventSourceResponse(event_generator())
