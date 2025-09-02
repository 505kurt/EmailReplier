from fastapi import APIRouter

from app.schemas.email_schema import EmailRequest, EmailResponse
from app.services.openai_service import generate_replies

router = APIRouter(
    prefix="/api",
    tags=["email"]
)

@router.post("/generate-replies", response_model=EmailResponse)
async def generate_email_replies(request: EmailRequest):
    """
    Recebe um e-mail e retorna 3 respostas geradas pelo OpenAI
    """
    replies = generate_replies(request)
    return replies