'''
import re 
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen

book_url = 'https://www.hetubook.com/book/4750/'
response_1 = requests.get(book_url) 
response_1.encoding = 'utf8'
# print(response_1.text)
# regx = '<a href=\"(.*)\" title=\"(.*)\"'
regx = 'title=\"(.*)\">'
result = re.findall(regx,response_1.text)

# print(result  )

#---
html_content = urlopen(book_url)
# r = requests.get(book_url)
soup = BeautifulSoup(html_content.read(),'lxml')
for cont in soup.find_all("a"):
	print(cont['title'])
'''
 
 
 

 