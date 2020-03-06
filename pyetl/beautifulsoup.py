from urllib import request
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req).read().decode('utf8')

soup = BeautifulSoup(res, 'html.parser')
#print(soup)

Logo=soup.findAll('a',{'id':'logo'})
print(Logo[0].text)
print(Logo[0].string)
print(Logo[0]['href'])

