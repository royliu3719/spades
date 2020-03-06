from urllib import request
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req).read().decode('utf8')

soup = BeautifulSoup(res, 'html.parser')

# --- 得到list
title =soup.findAll('div', class_='title')
#print(title)

#print(title[0])
#each_title = title[0].findAll('a')
#print(each_title[0].text)


# --- 用 for 迴圈取出 list 裏頭的所有物件
for title_html in title:
    try:
        print(title_html.findAll('a')[0].text)
    except IndexError as e:
        print(e.args)
    print('==============')



