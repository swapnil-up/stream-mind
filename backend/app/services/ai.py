from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=settings.OPENAI_API_KEY
)

async def stream_ai_response(prompt: str):
    stream = await client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[{
            "role": "user",
            "content": prompt
        }],
        stream=True,
    )
    
    async for chunk in stream:
        token = chunk.choices[0].delta.content
        if token:
            yield(token)
    yield "[DONE]"