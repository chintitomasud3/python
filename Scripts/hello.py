#import library
#....................
import requests
from bs4 import BeautifulSoup
import pandas as pd
import operator
from collections import Counter
import os
#.....................................

### Retrive data from url and parsing

def start(url):
    wordlist = []
    alllinks=[]
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        alllinks.append(link.get("href"))
    print("site name : {} and total links:  {}".format(source_code.url, len(alllinks)))
    print("Path file : {}".format(os.getcwd()))


start("https://www.geeksforgeeks.org")
start("https://www.google.com")

sites = requests.get("https://www.geeksforgeeks.org//")
soup = BeautifulSoup(sites.text, 'html.parser')

normalarray = [34, 22, 13, 45, 56, 12]
multiplearray=[["masud",213]]
df = pd.DataFrame(multiplearray,columns=["name","age"])
print(df)
#..........................................

