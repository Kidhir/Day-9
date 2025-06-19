# agents/alt_generator.py without @tool
import os
import warnings
from langchain.chat_models import ChatOpenAI
from state import GraphState

def generate_alt_text(state: GraphState) -> GraphState:
    image_urls = state.images
    context = state.context
    openai_key = os.getenv("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")
    if not openai_key:
        warnings.warn("OPENAI_API_KEY not set. Returning fallback alt text.")
        return state.copy(update={"alt_texts": ["[No Key] Alt text generation skipped."] * len(image_urls)})

    llm = ChatOpenAI(temperature=0.3, openai_api_key=openai_key)
    alt_texts = []
    for url in image_urls:
        prompt = f"Generate WCAG-compliant alt text for this image: {url}. Context: {context}"
        alt_text = llm.predict(prompt)
        alt_texts.append(alt_text)

    return state.copy(update={"alt_texts": alt_texts})
