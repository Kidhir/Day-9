# agents/rag_retriever.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load local model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample best practices (you can load more from a file)
WCAG_BEST_PRACTICES = [
    "Describe the content and function of the image clearly.",
    "Do not use phrases like 'image of' or 'picture of'.",
    "Be concise and accurate.",
    "If the image is decorative, use an empty alt attribute.",
    "Include visible text in the image if it is important."
]

# Generate embeddings once
pattern_embeddings = model.encode(WCAG_BEST_PRACTICES)

def retrieve_best_practices(generated_alt_text):
    input_embedding = model.encode([generated_alt_text])
    similarities = cosine_similarity(input_embedding, pattern_embeddings)[0]
    best_match_index = similarities.argmax()
    best_tip = WCAG_BEST_PRACTICES[best_match_index]

    # Return revised alt text with hint (simplified)
    return f"{generated_alt_text} ({best_tip})"
