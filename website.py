import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.flipkart.in/'
reqs=requests.get(url) # we are trying to open with website
soup=BeautifulSoup(reqs.text,'html.parser') #html.parser enabels the websitr
alllinks=[]
fv=open("G:\\website.Txt","a")
for link in soup.find_all('a'):   #any link <A href="x">
       print(link.get('href'))
       alllinks.append(link)
for  x in alllinks:
       fv.write(str(x)+"\n")