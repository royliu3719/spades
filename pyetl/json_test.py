import requests
import json
from urllib import request
import os

# 指定圖片資料夾
if not os.path.exists(r'./dcard_img'):
    os.mkdir(r'./dcard_img')


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232762503'
res = requests.get(url,headers=headers)
print(res.text) # res整頁的字串

tmp_json = json.loads(res.text) # 用json.loads將字串轉成json格式(由字典和list組成)
#print(tmp_json)

for each_title in tmp_json:

    article_title = each_title['title'].replace('/','') # p137以文章的標題當作檔名
    if not os.path.exists('./dcard_img/%s'%(article_title)):
        os.mkdir(r'./dcard_img/%s'%(article_title))

    print(article_title)
    print('https://www.dcard.tw/f/photography/p/' + str(each_title['id'])) # id是數字, 要轉成str

    for img_url_dict in each_title['mediaMeta']: # print(each_title['mediaMeta']) # 每一張圖片的List
        img_url_dict = img_url_dict['url']
        try:
            request.urlretrieve(img_url_dict, r'./dcard_img/%s/%s'%(article_title, img_url_dict.split('/')[-1])) # p137設定圖片存放位置
        except:
            pass
        print('\t%s'%(img_url_dict))

print()