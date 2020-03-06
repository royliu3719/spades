import requests
from urllib import request
from bs4 import BeautifulSoup
import os

# 指定圖片資料夾
if not os.path.exists(r'./ptt_img'):
    os.mkdir(r'./ptt_img')

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

ss = requests.session()
ss.cookies['over18'] = '1'

page = 7000
for i in range(0, 10):
    url = 'https://www.ptt.cc/bbs/Food/index%s.html'%(page)

    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div[class="title"] a')



    for each_title in title:
        print(each_title.text)

        article_url = ('https://www.ptt.cc' + each_title['href'])
        print(article_url)

        res_article = ss.get(article_url, headers=headers)

        article_soup = BeautifulSoup(res_article.text, 'html.parser')

        url_list = article_soup.select('div [id="main-content"] a')
        # print(url_list)


        page -= 1


        for each in url_list:

            #print(each.text)

            try:
                if each.text.split('.')[-1] == 'jpg':
                    request.urlretrieve(each.text, r'./ptt_img/%s' % (each.text.split('/')[-1]))
                    # print(each.text.split('/')[-1])
            except:
                pass






