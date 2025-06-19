# agents/image_scanner.py

from bs4 import BeautifulSoup
import requests

def scan_images(url):
    """Scans the given URL and returns a list of images without or with poor alt text"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = []

    for img in soup.find_all('img'):
        alt = img.get('alt', '').strip().lower()
        if not alt or alt in ['image', 'photo', 'picture', '']:
            images.append({
                'src': img.get('src'),
                'alt': alt,
                'context': img.find_parent().get_text()[:150] if img.find_parent() else ''
            })

    return images
