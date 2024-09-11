import requests
from bs4 import BeautifulSoup
import time


def get_links_from_page(url):
    links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for td in soup.find_all('td', class_='title'):
        a_tag = td.find('a')
        if a_tag and a_tag.get('href'):
            link = a_tag['href']
            title = a_tag.text.strip()
            
            if link.startswith('item?id='):
                link = f'https://news.ycombinator.com/{link}'
            elif not link.startswith('http'):
                link = f'https://news.ycombinator.com/{link}'
            
            links.append({'url': link, 'title': title})
    
    return links

def get_all_links(base_url, pages=1):
    """"
    base_url = main url that contain links to the articles
    pages = number of pages that will be gather the articles
    """
    all_links = []
    #iterate over pages
    for i in range(pages):
        url = f"{base_url}?p={i+1}"
        #get all the links from the page in the range
        links = get_links_from_page(url)
        #commit the links in the list
        all_links.extend(links)
        time.sleep(2)
    return all_links
