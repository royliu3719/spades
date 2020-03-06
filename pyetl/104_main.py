import requests
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
keyword = '大數據'

practice_104_list = [
    ['公司名稱', '職缺名稱', '工作內容', '需要工具', '工作技能', '聯絡人員', '招聘網址', '技能總數'],
        ]


list_skill = ['公司名稱', '職缺名稱', '工作內容', '需要工具', '工作技能', '聯絡人員', '招聘網址', '技能總數']
word_count = {}

for i in range(0, 1):
    # print("run in loop!")
    url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%s&order=12&asc=0&page=%s&mode=s&jobsource=2018indexpoc'%(keyword, i)
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())
    title = soup.select('div[class="b-block__left"] a')
    # print(title)

    for each_title in title:
        try:
            if 'job' == each_title['href'].split('/')[3]:
                # print('https:'+each_title['href'])
                article_url = ('https:' + each_title['href'])

                res_article = requests.get(article_url, headers=headers)
                # print(res_article)
                article_soup = BeautifulSoup(res_article.text, 'html.parser')
                # print(article_soup)
                ul = article_soup.select('div[class="center"] h1')
                sv = article_soup.select('dd[class="tool"]')[0]
                sv1 = article_soup.select('dd[class="tool"]')[1]
                con = article_soup.select('div[class="content"]')[3]('dd')[0]
                tem_str = article_soup.select('dd[class="tool"]')[0].text
                work = article_soup.select('section[class="info"] p')[0].text.replace('\r', '').replace(',', '').replace('●', '')
                # print(work)

                s_list = tem_str.split('、')

                for j in s_list:
                    if j in word_count:
                        word_count[j] += 1
                    else:
                        word_count[j] = 1
                # print(word_count)

                # 判斷是否為不拘，並且計算所需技能的總數
                if tem_str == '不拘':
                    g = 0
                else:
                    g = len(tem_str.split('、'))
                    for i in tem_str.split('、'):
                        if i not in list_skill:
                            list_skill.append(i)
                # print(list_skill)

                # print('公司名稱 :', ul[0].text.split('\n')[2].strip())
                # print('職缺名稱 :', ul[0].text.split('\n')[1].strip())
                # print('需要工具 :', sv.text)
                # print('工作技能 :', sv1.text)
                # print('聯絡人員 :', con.text)
                # print('招聘網址 :', article_url)
                # print()
                a = ul[0].text.split('\n')[2].strip()
                b = ul[0].text.split('\n')[1].strip()
                c = sv.text
                d = sv1.text
                e = con.text
                f = article_url

                practice_104_list.append([a, b, work, c, d, e, f, g])
                # print(practice_104_list)

        except:
            pass
# print(practice_104_list)

practice_104_list[0] = list_skill

# print(practice_104_list[0])
# 開檔並且寫入，最後做一個關閉的動作
with open('practice_104.csv', mode='w', encoding='utf8') as f:
    for line in range(len(practice_104_list)):
        text = str(practice_104_list[line]) \
                   .replace('[', '').replace(']', '').replace('\'', '') + '\n'

        f.write(text)
    else:
        print('ok')
    f.close()

# 統計每項技能的次數，然後去做排序
word_count = [(k, word_count[k]) for k in word_count]
word_count.sort(key=lambda x: x[1], reverse=True)
# print(word_count)
# print(list_skill)
#
# o = practice_104_list[0]
# print(o)
