from urllib import request
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req).read().decode('utf8')

soup = BeautifulSoup(res, 'html.parser')

# ------ select 用法
title =soup.select('div[class="title"] a')
for each_title in title:
    print(each_title.text)
    print('https://www.ptt.cc'+ each_title['href'])


