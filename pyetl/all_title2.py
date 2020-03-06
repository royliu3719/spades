from urllib import request
from bs4 import BeautifulSoup
import requests


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = 1
for i in range(0, 1):
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page)

    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(res, 'html.parser')




    title =soup.select('div[class="title"] a')

    for each_title in title:
        print(each_title.text)
        try:
            article_url = ('https://www.ptt.cc'+ each_title['href'])
            print(article_url)
            res_article = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(res_article.text, 'html.parser')
            
        except KeyError as e:
            print(e.args)
        print()

    url_list = soup.select('div [class="btn-group btn-group-paging"] a[class="btn wide"]')
    url = 'https://www.ptt.cc' + url_list[1]['href']
