from bs4 import BeautifulSoup
import requests
 
params = {'q': "pizza"}
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
r = requests.get('https://www.bing.com/search', headers=headers, params=params)
 
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})
 
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
 
    if item_text and item_href:
        print(item_text)
        print(item_href)