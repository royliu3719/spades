import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'http://8f7c891f.ngrok.io/hello_post'

post_data = {'username':'帥哥'}

res = requests.post(url, headers=headers, data=post_data)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup)

