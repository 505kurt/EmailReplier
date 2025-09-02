from openai import OpenAI
from dotenv import load_dotenv

import os

from app.schemas.email_schema import EmailRequest, EmailResponse

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_response(email:EmailRequest, system_prompt:str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": email.email_text,
            }
        ]
    )

    return response.choices[0].message.content


def generate_replies(email: EmailRequest):
    system_prompts = [
        "Responda esse e-mail de forma cordial e profissional, no idioma original, mantendo comunicação técnica e detalhista se necessário.",
        "Responda esse e-mail de forma profissional mas em um tom mais leve, mantendo seu idioma original e utilizando expressões típicas do ambiente executivo.",
        "Responda esse e-mail em tom informal, mantendo seu idioma original e utilizando expressões populares."
    ]

    responses = []

    for i in range(0, 3):
        responses.append(generate_response(email, system_prompts[i]))

    replies = EmailResponse(email_response = responses)

    return replies


if __name__ == "__main__":
    email = EmailRequest(email_text = "Olá, gostaria de saber se vocês têm disponibilidade para uma reunião na próxima semana para discutirmos uma possível parceria. Quais seriam os melhores horários para vocês?")

    print(generate_replies(email).email_response)