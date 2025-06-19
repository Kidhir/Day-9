# Refactored agents/review.py
from langchain.agents import tool

@tool
def review_generated_text(alt_text: str) -> str:
    """Provides an editable interface or review comments for alt text."""
    return f"Suggested alt text: {alt_text}. You may edit before publishing."
