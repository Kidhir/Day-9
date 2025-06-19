# Refactored agents/alt_generator.py with API key handling
import os
from langchain.agents import tool
from langchain.chat_models import ChatOpenAI

openai_key = os.getenv("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")
if not openai_key:
    raise ValueError("Missing OPENAI_API_KEY. Please set it in your environment or Streamlit secrets.")

llm = ChatOpenAI(temperature=0.3, openai_api_key=openai_key)

@tool
def generate_alt_text(image_url: str, context: str = "") -> str:
    """Generates WCAG-compliant alt text for a given image using optional context."""
    prompt = f"Generate WCAG-compliant alt text for this image: {image_url}. Context: {context}"
    return llm.predict(prompt)
