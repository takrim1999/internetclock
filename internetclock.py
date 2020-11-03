import requests
from bs4 import BeautifulSoup
try:
    place = input("place you want to search?\n>")
    place = "+".join(place.split())

    header = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    responce = requests.get("http://google.com/search?q=what's+the+time+now+in+" + place)
    content = responce.text
    soup = BeautifulSoup(content , "lxml")
    for k in soup.find_all("b"):
        print(f"thought you searched for \"{k.text}\" so,")
    for i in soup.find_all("div"):
        if ("PM" in i.text or "AM" in i.text) and len(i.text)<9:
            print(f"time is : {i.text}")
            break
except:
    print("not connected to the internet")


