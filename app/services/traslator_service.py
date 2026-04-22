from deep_translator import GoogleTranslator


class TranslatorService:
    @staticmethod
    def translate_text(text: str, target_language: str, source_language: str = "auto") -> str:
        """
        Traduce un texto usando GoogleTranslator de deep-translator.
        """
        translator = GoogleTranslator(source=source_language, target=target_language)
        return translator.translate(text)