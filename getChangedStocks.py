import requests
import changedStockEntity
import chardet
from changedStockEntity import ChangedStock 
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def getPage(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    page = driver.page_source.encode('utf-8')
    return page

def getChangedStocks(html):
    soup = BeautifulSoup(html, 'html.parser')
    stocks = []
    tbody = soup.find('tbody')
    if not tbody:
        return stocks
    trs = tbody.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        stock = ChangedStock(tds[0].get_text(), tds[1].get_text(), 
        tds[2].get_text(), tds[3].get_text(), tds[4].get_text())
        stocks.append(stock)
    return stocks

def printStocks():
    url = 'https://kabu.com/investment/meigara/tani_henkou.html'
    page = getPage(url)
    stocks = getChangedStocks(page)
    for stock in stocks:
        print(stock)

printStocks()