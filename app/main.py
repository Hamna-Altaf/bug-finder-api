from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.logic import analyze_code
from app.sampleCases import sample_cases
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import FastAPI, Request
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from fastapi import Query

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many requests. Please slow down. Only 5 requests per minute per IP."},
    )

#This class will hold the input data for the API
class CodeInput(BaseModel):
    language: str
    code: str

#Main method to check for bugs in the code
@app.post("/find-bug")
@limiter.limit("5/minute")
def find_bug(request: Request, data: CodeInput, mode: str = Query("developer", enum=["developer", "casual"])) -> dict:
    if not data.language or not data.code:
        raise HTTPException(status_code = 400, detail="Language and code both are required")
    
    if len(data.code.splitlines()) > 30:
        raise HTTPException(status_code = 400, detail="Code should be of 30 lines or less")
    

    result = analyze_code(data.language, data.code, mode)
    return result

#returns a few fixed examples by sample cases
@app.get("/sample-cases")
def get_sample_cases():
    return sample_cases