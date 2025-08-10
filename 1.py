from bs4 import BeautifulSoup
import requests
w=requests.get("https://fararu.com")
soup=BeautifulSoup(w.content)
divs=soup.find_all("div",{"class":"same_box same_header"})
div=divs[1]
links=div.find_all("a")
for link in links:
    p=("https://fararu.com"+link["href"]+"\n")
    #print(p)
    q=requests.get(p)
    soup=BeautifulSoup(q.content)
    divs=soup.find_all("div",{"class":"primary_files"})
    for div in divs:
        links=div.find_all("img")
        for link in links:
            print(link["src"],"\n")