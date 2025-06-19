# Refactored agents/alt_generator.py with lazy loading and fallback
import os
import warnings
from langchain.agents import tool
from langchain.chat_models import ChatOpenAI

@tool
def generate_alt_text(image_url: str, context: str = "") -> str:
    """Generates WCAG-compliant alt text for a given image using optional context."""
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        warnings.warn("OPENAI_API_KEY not set. Returning fallback message.")
        return "[No API Key] Alt text generation skipped."

    llm = ChatOpenAI(temperature=0.3, openai_api_key=openai_key)
    prompt = f"Generate WCAG-compliant alt text for this image: {image_url}. Context: {context}"
    return llm.predict(prompt)
