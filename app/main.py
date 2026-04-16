from fastapi import FastAPI
from app.schemas.traslater import TranslationRequest, TranslationResponse
from app.services.traslator_service import TranslatorService
from app.routes.health import router as health_router

app = FastAPI(
    title="Mi API con FastAPI",
    version="1.0.0",
    description="API base montada con FastAPI"
)

app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "FastAPI funcionando correctamente"}

@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    try:
        translated_text = TranslatorService.translate_text(
            text=request.text,
            target_language=request.target_language,
            source_language=request.source_language
        )

        return TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            source_language=request.source_language,
            target_language=request.target_language
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al traducir: {str(e)}")