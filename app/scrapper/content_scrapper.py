import requests
from bs4 import BeautifulSoup
from readability import Document  # Requires readability-lxml
from newspaper import Article  # Requires newspaper3k

def find_content_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Attempt to extract main content using readability or newspaper
    content = ""
    try:
        # Using readability library
        doc = Document(response.text)
        content = doc.summary()
    except Exception as e:
        print(f"Readability extraction failed: {e}")
    
    if not content:
        # Fallback to newspaper library if readability fails
        try:
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
        except Exception as e:
            print(f"Newspaper extraction failed: {e}")
    
    # Extract tags if available; this is site-specific
    tags = []
    try:
        # Example for common tag patterns; adjust based on site structure
        for a in soup.find_all('a', class_='tag'):
            tags.append(a.get_text())
        
        # Example for another common pattern
        for meta in soup.find_all('meta', {'name': 'keywords'}):
            if 'content' in meta.attrs:
                tags.extend(meta['content'].split(','))
    except Exception as e:
        print(f"Tag extraction failed: {e}")
    
    return content, tags