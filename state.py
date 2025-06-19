from pydantic import BaseModel
from typing import List

class GraphState(BaseModel):
    url: str
    context: str = ""
    result: str = ""
    images: List[str] = []
    alt_texts: List[str] = []
    best_practices: str = ""
    reviewed_output: List[str] = []