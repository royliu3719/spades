import requests
from bs4 import BeautifulSoup
import os
import re
from time import sleep

path = r'E://專題//mobile01'
if not os.path.exists(path):
    os.mkdir(path)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win6'
                        '4; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

# cookie
cookie_tmp = 'cookie: _ss_pp_id=2395f69c9296bb600b94a34e1627754c; __gads=ID=b4b47e8475118749:T=1576117373:S=ALNI_MbjO55UJ9FfU6BSjdLPcW_g5-uofw; _ga=GA1.2.650854042.1576117374; _gcl_au=1.1.1781855618.1576117374; dable_uid=61548017.1575338715704; _td=c3aa65c6-e666-4be7-b459-a69a886a2765; MID_uuid=0103fdc0-3b1f-11ea-81e8-137f0fa9be91; PHPSESSID=2f772e9205db5f8e326caa4f1126144b; ad_header_10=1; _gid=GA1.2.1231276726.1581919112; ad_header_index=2; _gat_UA-121129530-1=1; _gat_UA-121129530-3=1; _gat_UA-124523494-1=1; _gat_UA-124523494-2=1; _gat_UA-808494-1=1'
# 整理 cookie 成字典格式
cookie = {}
for i in cookie_tmp.split(";"):
    cookie[i.split("=")[0]] = i.split("=")[1]

count = 0

for i in range(268, 417):
    url = 'https://www.mobile01.com/topiclist.php?f=189&p=' + str(i)

    res = requests.get(url, headers=headers, cookies=cookie)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div[class="c-listTableTd__title"] a[class="c-link u-ellipsis"]')

    for j in title:
        url_article = "https://www.mobile01.com/" + j['href']
        tit = re.search("&t=(.*)", url_article)

        article = ""
        page_count = 1

        while True:
            url_page = url_article + "&p=" + str(page_count)
            res_page = requests.get(url_page, headers=headers, cookies=cookie)
            soup_page = BeautifulSoup(res_page.text.replace("<br>", "\n"), 'html.parser')

            test404 = soup_page.select('div[class ="o-fNotes"]')
            if len(test404) == 1:
                break

            [s.extract() for s in soup_page.select('blockquote')]
            content = soup_page.select('article')
            # print(url_page)

            for k in range(len(content)):
                article += content[k].text.lstrip()
                article += "\n" + "----\n\n"
            page_count += 1



        try:
            with open(path + '/' + tit.group(1) + '.txt', 'w', encoding='utf8') as f:
                f.write(article)
            count += 1
        except Exception as err:
            print(err)
            print(url_page)

    print("第" + str(i) + "頁")
    sleep(10)


