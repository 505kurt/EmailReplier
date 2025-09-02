from pydantic import BaseModel
from typing import List


class EmailRequest(BaseModel):
    email_text: str


class EmailResponse(BaseModel):
    email_response: List[str]