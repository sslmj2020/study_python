import requests
from bs4 import BeautifulSoup
import lxml
url='https://news.qq.com'
r=requests.get(url,timeout=30)
a=r.text
print(a)
soup=BeautifulSoup(a,'lxml')
soup.prettify
print(soup.prettify)
print(soup.find_all('link',name_='text'))
'''for news in soup.find_all('div',class_='text'):
   info=news.find('a')
    title=info.get_text()
    link=str(info.get('href'))
    print('标题：'+title)
    print('链接：'+link+'\n')
    print('没有符合项')'''
                 
