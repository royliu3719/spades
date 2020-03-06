import requests
from bs4 import BeautifulSoup
import os

path = r'E://專題//pixnet'
if not os.path.exists(path):
    os.mkdir(path)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
search_tag = '台北景點'  # 手動更改
url = 'https://www.pixnet.net/tags/%s'%(search_tag)

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)










































