import re
import requests
from bs4 import BeautifulSoup

def getWiki(links):
    wikiLinks = []
    regex = r'\bhttps?://en\.wikipedia\.org/wiki/([^\s/]+)'

    for link in links:
        if link[:6]=='/wiki/':
            if ':' in link or 'main_page' in link or 'Main_Page' in link:
                continue
            l = 'https://en.wikipedia.org'+link
            wikiLinks.append(l)
            continue
        match = re.match(regex, link)
        if match:
            wikiLinks.append(link)

    return wikiLinks

def extract_links_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    
    return links