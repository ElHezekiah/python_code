import requests
from bs4 import BeautifulSoup

page=requests.get('https://shopee.co.id/?gad_source=1&gad_campaignid=1558961180&gbraid=0AAAAADPpU80zZUmP2m3H5Gv-RE74TFgul&gclid=CjwKCAjw687NBhB4EiwAQ645diJjulHk-6TzkSU0s1pENzYiQe-q2gpCMkDhv5vn90zKlxV2CfjN4hoC4tIQAvD_BwE')
soup=BeautifulSoup(page.text,'html.parser')
if page.status_code==200:
    print("success")
artcles = soup.find_all('p')
for p in artcles:
    print(p.text)