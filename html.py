#check whether the html element or not 
# import urllib3
# from bs4 import BeautifulSoup
# http=urllib3.PoolManager()
# r=http.request('GET',"https://tutorialpoints.com")
# soup=BeautifulSoup(r.data,features="html5lib")
# print(soup.title)
# print(soup.title.text)




import urllib3
from bs4 import BeautifulSoup
http =urllib3.PoolManager()
r=http.request('GET','https://geeksforgeeks.org')
soup=BeautifulSoup(r.data ,features="html5lib")
print(soup.title)
print(soup.title.text)


# import urllib3
# from bs4 import BeautifulSoup
# http =urllib3.PoolManager()
# r=http.request('GET','https://geeksforgeeks.org')
# soup=BeautifulSoup(r.data ,features="html5lib")
# print(soup.title)
# print(soup.title.text)


import urllib3
from bs4 import BeautifulSoup

# Create a PoolManager instance to handle requests
http = urllib3.PoolManager()

# Make a request to the URL
r = http.request('GET', 'https://geeksforgeeks.org')

# Parse the HTML content of the page
soup = BeautifulSoup(r.data, features="html5lib")

# Print the title tag and its text content
print(soup.title)
print(soup.title.text)
