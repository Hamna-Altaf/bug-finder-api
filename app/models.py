from pydantic import BaseModel
from typing import Optional

class CodeInput(BaseModel):
    language: str
    code: str

class BugReport(BaseModel):
    language: str
    bugType: str
    description: str
    suggestion: Optional[str] = None
    