import  requests
from bs4 import BeautifulSoup
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())


if __name__ =='__main__':
     qiushibaike()
     print('hello word')