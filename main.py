from app.scrapper.scrapper import get_all_links
from app.scrapper.content_scrapper import find_content_articles

def main():
    base_url = 'https://news.ycombinator.com/'
    all_links = get_all_links(base_url, pages=1)  # Adjust pages as needed
    
    for link in all_links:
        content, tags = find_content_articles(link["url"])
        print(link["url"], link["title"], content, tags)

if __name__ == '__main__':
    main()
