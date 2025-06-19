# agents/review.py without @tool
from state import GraphState

def review_generated_text(state: GraphState) -> GraphState:
    reviewed = [f"Suggested alt text: {text}" for text in state.alt_texts]
    return state.copy(update={"reviewed_output": reviewed})
