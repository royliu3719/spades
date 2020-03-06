from urllib import request
from bs4 import BeautifulSoup
import requests

url = 'http://8f7c891f.ngrok.io/weather'
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}



post_url = 'https://works.ioa.tw/weather/img/weathers/zeusdesign/04@2x.png'

post_data_str = """location: 台北"""


post_data = {'location': '台北'}

res = requests.post(url, headers=headers, data=post_data)
soup = BeautifulSoup(res.text, 'html.parser')



print(soup.text)


