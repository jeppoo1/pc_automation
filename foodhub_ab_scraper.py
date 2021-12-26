### Web scraper for getting a week's menu for Ravintola FOODHUB ab Espoo


# Importing modules (BeautifulSoup)
import bs4
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import time


# Choosing the url
url = "https://www.sodexo.fi/ravintolat/ravintola-foodhub-ab"

### headers defines a dummy browser for this program to use. Without it, an error occurs, so use it!
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# Request the url for scraping
response = requests.get(url, headers=headers)
text = response.text

soup = BeautifulSoup(text, features = "lxml")

soup_meals = []
for i in range(0,1):
    soup_meals_item = str(soup.find_all('div', {"class" : "meal-name-wrapper"})) # extract meal type, example -----> <span class="meal-type">Dessert</span>
    soup_meals_item = soup_meals_item.replace('''[<div class="meal-name-wrapper">\n<span class="meal-type">''', "")
    soup_meals_item = soup_meals_item.replace('''</span>\n<p class="meal-name">''', ": ")
    soup_meals_item = soup_meals_item.replace('''<div class="meal-name-wrapper">\n<span class="meal-type">''', "\n")
    soup_meals_item = soup_meals_item.replace('''</p>\n</div>, ''', "")
    soup_meals_item = soup_meals_item.replace('''</p>\n</div>]''', "")
    soup_meals.append(soup_meals_item)

soup_days = []
for i in range(0,7): # extract days of the week and their dates
    soup_days_item = str(soup.find_all('a', {"href" : "#tabs-"+str(i)}))
    if i == 0:
        soup_days_item = soup_days_item.replace('''[<a href="#tabs-''' + str(i) + '''">''', "")
    else:
        soup_days_item = soup_days_item.replace('''[<a href="#tabs-''' + str(i) + '''">''', "\n")
    soup_days_item = soup_days_item.replace('''</a>]''', " ")
    soup_days.append(soup_days_item)

soup_meals2 = []

for i in soup_meals:
    item = i.split("\n")
    soup_meals2.append(item)

with open('foodhub_meals.txt', 'w', encoding="utf-8-sig", newline = '') as myfile:
    for a in soup_days:
        myfile.write(a + "\n")
        for i in soup_meals2[0]:
            myfile.write(i + "\n")
            if 'Dessert' in i:
                del soup_meals2[0][:8]
                break
    myfile.write("\n")
    print("\nFinished writing to", myfile, "\n")


# Search the text file for a specific word / meal

import regex
import colorama
from colorama import init
init()
from colorama import Fore, Style

search_list = []
with open('foodhub_meals.txt', 'r', encoding="utf-8-sig", newline = '') as myfile:
    user_favorite = str(input("Lempiruokasi? (esim. kana/liha/kala/peruna/riisi/soup/dessert). Paina enter jos haluat pelkän ruokalistan.\n"))
    text = (myfile.read().splitlines())
    if user_favorite == "":
        print("Painoit enter. Tässä tämän viikon ruokalista ravintolalle Sodexo AB Keilaranta Espoo:\n")
        for line in text:
            if ("La ") in line or ("Su ") in line:
                break
            else:
                print(line)
    else:
        print("Hakusanasi on", Fore.MAGENTA + Style.BRIGHT + user_favorite + Style.RESET_ALL + ". Tässä tämän viikon ruokalistasta löytyneet tulokset ravintolalle Sodexo AB Keilaranta Espoo:\n")
        for line in text:
            search_list.append(line)
            if ("Tänään ") in line or ("Ma ") in line or ("Ti") in line or ("Ke ") in line or ("To ") in line or ("Pe ") in line:
                print(line)
            if ("La ") in line or ("Su ") in line:
                break
            if re.findall('(?i)'+user_favorite, str(line)): # if re.findall(user_favorite, str(line), flags=re.IGNORECASE): # ignorecase also works as following: re.findall('(?i)my_text', "text where my_TeXt is found")
                print(Style.RESET_ALL, (Fore.CYAN + line + Style.RESET_ALL), Fore.YELLOW + "\n_____________________________________________________\n" + Style.RESET_ALL)
    if not re.findall('(?i)' + user_favorite, (' '.join(i for i in search_list))):
            print(Fore.YELLOW + "****" + Style.RESET_ALL + "Lempiruokaasi ei ole tällä viikolla tarjolla." + Fore.YELLOW + "****" + Style.RESET_ALL)