# Refactored agents/alt_generator.py
from langchain.agents import tool
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.3)

@tool
def generate_alt_text(image_url: str, context: str = "") -> str:
    """Generates WCAG-compliant alt text for a given image using optional context."""
    prompt = f"Generate WCAG-compliant alt text for this image: {image_url}. Context: {context}"
    return llm.predict(prompt)
