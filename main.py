import wikipedia

from breadthFirstSearch import breadthFirstSearch
import requests
import json

src = input("Enter the source article title: ")
api_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={src}"
response = requests.get(api_url)
data = response.json()
src = data[3][0]

print(src)


dest = input("Enter the destination article title : ")
api_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search={dest}"
response = requests.get(api_url)
data = response.json()
dest = data[3][0]

print(dest)

visited = {}
path = breadthFirstSearch(src,dest,visited)

if path[0]=="Not in next 5 levels":
    print("Not in range")
else:
    path.reverse()
    print(path)