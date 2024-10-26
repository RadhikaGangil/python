import urllib3
from bs4 import BeautifulSoup
http =urllib3.PoolManager()
r=http.request('GET','https://geeksforgeeks.org')
soup=BeautifulSoup(r.data ,features="html5lib")
print(soup.title)
print(soup.title.text)