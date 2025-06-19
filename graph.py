# graph.py
from langgraph.graph import StateGraph, END
from langchain.agents import Tool
from agents.image_scanner import scan_images
from agents.rag_retriever import retrieve_best_practices
from agents.alt_generator import generate_alt_text
from agents.review import review_generated_text

# Wrap tools as LangGraph-compatible agents
tools = [
    Tool.from_function(scan_images),
    Tool.from_function(retrieve_best_practices),
    Tool.from_function(generate_alt_text),
    Tool.from_function(review_generated_text)
]

# Define the agent-based flow using StateGraph
graph = StateGraph()

graph.add_node("ScanImages", scan_images)
graph.add_node("RetrievePatterns", retrieve_best_practices)
graph.add_node("GenerateAlt", generate_alt_text)
graph.add_node("Review", review_generated_text)

# Define transitions
graph.set_entry_point("ScanImages")
graph.add_edge("ScanImages", "RetrievePatterns")
graph.add_edge("RetrievePatterns", "GenerateAlt")
graph.add_edge("GenerateAlt", "Review")
graph.add_edge("Review", END)

# Compile the final graph
final_graph = graph.compile()
