from bs4 import BeautifulSoup
import requests
w=requests.get("https://fararu.com")
soup=BeautifulSoup(w.content)
divs=soup.find_all("div", {"class":"same_box same_header"})
div=divs[1]
links=div.find_all("a")
seen_img=[]
for link in links:
    p="https://fararu.com"+link["href"]
    q=requests.get(p)
    soup=BeautifulSoup(q.content)
    divs=soup.find_all("div",{"class":"primary_files"})
    for div in divs:
        imgs=div.find_all("img")
        for img in imgs:
            src=img.get("src")
            if src not in seen_img:
                seen_img.append(src)
                print(src)