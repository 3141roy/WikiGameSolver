from extractLinks import extract_links_from_webpage
from extractLinks import getWiki
from extractPath import extractPath

from queue import Queue
import re
import requests
from bs4 import BeautifulSoup


parent = {}
def breadthFirstSearch(src,dest,visited):
    q = Queue()
    q.put(src)
    visited[src]=True
    parent[src] = None
    level = 0
    while(q.qsize()>0):
        n = q.qsize()
        level+=1
        if level==6:
            return ["Not in next 5 levels"]
        for i in range(n):
            curr = q.get()
            print(curr)
            if(curr==dest):
                return extractPath(parent,src,dest)

            allLinks = extract_links_from_webpage(curr)
            wikiLinks = getWiki(allLinks)
            for link in wikiLinks:
                if link in visited:
                    continue
                visited[link]=True
                parent[link] = curr

                q.put(link)
