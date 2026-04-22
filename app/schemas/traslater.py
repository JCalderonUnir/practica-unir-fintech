from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Texto a traducir")
    target_language: str = Field(..., min_length=2, description="Idioma destino, por ejemplo: en, es, fr")
    source_language: str = Field(default="auto", min_length=2, description="Idioma origen o 'auto'")


class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    source_language: str
    target_language: str