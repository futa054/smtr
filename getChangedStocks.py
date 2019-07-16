import requests
import changedStockEntity
import chardet
from bs4 import BeautifulSoup

def getChangedStocks(url):
    req = requests.get(url)
    req.encoding = chardet.detect(req.content)['encoding']
    soup = BeautifulSoup(req.text, 'html.parser')
    stocks = []
    tbody = soup.find('div', attrs={'id': 'content'})
    print(tbody)
    if not tbody:
        return stocks
    trs = tbody.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
    return stocks

def printStocks():
    url = 'https://kabu.com/investment/meigara/tani_henkou.html'
    stocks = getChangedStocks(url)

printStocks()