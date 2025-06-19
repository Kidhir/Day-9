# Refactored agents/image_scanner.py
from langchain.agents import tool
import requests
from bs4 import BeautifulSoup

@tool
def scan_images(url: str) -> list:
    """Scans a webpage and returns a list of image URLs."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return [img['src'] for img in soup.find_all('img') if img.get('src')]
    except Exception as e:
        return [f"Error scanning images: {str(e)}"]
