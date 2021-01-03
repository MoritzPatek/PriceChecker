import requests
from bs4 import BeautifulSoup

#thats the product we want to check on amazon
URL = 'https://www.amazon.de/Apple-Watch-Aluminiumgeh%C3%A4use-Space-Sportarmband-Schwarz/dp/B08J6HN3CH/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=LWGT2W1H53B3&dchild=1&keywords=apple+watch+6&qid=1609695253&sprefix=apple+watch+%2Caps%2C266&sr=8-1'

#you can just google your header with 'whats my header'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def getPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    pricetxt = soup.find(id='priceblock_ourprice').get_text()[:-2].replace(',', '.')
    title = soup.find(id='productTitle').get_text()
    return float(pricetxt)

#init price so we can check if the product got cheaper
initPrice = getPrice()


def checkPrice():
    newPrice = getPrice()
    if newPrice < initPrice:
        sendMail(initPrice-newPrice)

def sendMail(price):
    print("i really want an apple watch")

