# agents/image_scanner.py using GraphState (no @tool)
import requests
from bs4 import BeautifulSoup
from state import GraphState

def scan_images(state: GraphState) -> GraphState:
    """Scans a webpage and returns a list of image URLs."""
    try:
        response = requests.get(state.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_urls = [img['src'] for img in soup.find_all('img') if img.get('src')]
        return state.copy(update={"images": image_urls})
    except Exception as e:
        return state.copy(update={"images": [f"Error scanning images: {str(e)}"]})
