import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()
ss.cookies['over18']= '1'


res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

print(ss.cookies)

#print(soup.prettify())

