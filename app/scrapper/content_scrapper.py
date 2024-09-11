import requests
from bs4 import BeautifulSoup
import time


def find_content_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract content; this will vary based on the site’s HTML structure
    content = ""
    if 'item?id=' in url:
        content_div = soup.find('div', class_='comment')
        if content_div:
            content = content_div.get_text(separator="\n").strip()
    
    # Extract tags if available; this is site-specific
    tags = []
    for a in soup.find_all('a', class_='tag'):
        tags.append(a.get_text())
    
    return content, tags