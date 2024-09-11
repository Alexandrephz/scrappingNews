from app.scrapper.scrapper import get_all_links

def main():
    base_url = 'https://news.ycombinator.com/'
    all_links = get_all_links(base_url, pages=1)  # Adjust pages as needed
    
    for link in all_links:
        print(link)

if __name__ == '__main__':
    main()
