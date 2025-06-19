from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from agents.image_scanner import scan_images
from agents.rag_retriever import retrieve_best_practices
from agents.alt_generator import generate_alt_text
from agents.review import review_generated_text

# Define state schema (you can expand this later)
class GraphState(BaseModel):
    url: str
    context: str = ""
    result: str = ""

# Build graph with schema
graph = StateGraph(GraphState)

graph.add_node("ScanImages", scan_images)
graph.add_node("RetrievePatterns", retrieve_best_practices)
graph.add_node("GenerateAlt", generate_alt_text)
graph.add_node("Review", review_generated_text)

graph.set_entry_point("ScanImages")
graph.add_edge("ScanImages", "RetrievePatterns")
graph.add_edge("RetrievePatterns", "GenerateAlt")
graph.add_edge("GenerateAlt", "Review")
graph.add_edge("Review", END)

final_graph = graph.compile()
