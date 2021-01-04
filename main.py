#so yeah i really want an apple watch, but i am super broke, so the only logical way to handle that is to programm a bot
#that keeps track of the price of the product - yeah I REALLY want that apple watch lol

import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import smtplib
#thats the product we want to check on amazon
URL = 'https://www.amazon.de/Apple-Watch-Aluminiumgeh%C3%A4use-Space-Sportarmband-Schwarz/dp/B08J6HN3CH/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=LWGT2W1H53B3&dchild=1&keywords=apple+watch+6&qid=1609695253&sprefix=apple+watch+%2Caps%2C266&sr=8-1'

#you can just google your header with 'whats my header'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def getPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    pricetxt = soup.find(id='priceblock_ourprice').get_text()[:-2].replace(',', '.')
    return float(pricetxt)

#init price so we can check if the product got cheaper
initPrice = getPrice()


def checkPrice():
    newPrice = getPrice()
    if newPrice < initPrice:
        sendMail(newPrice)

#as soon as the bot detects that the price drops, it creates a mail and sends it to your email

def sendMail(currentPrice):
    msg = EmailMessage()
    msg.set_content("Alert!!! - the product with the price "+str(initPrice)+" got cheaper!"+" The current price is "+str(currentPrice)+", thats "+str(initPrice-currentPrice)+"less!!")
    msg['to'] = "TheMailThatShouldGetTheAlert"
    msg['subject'] = "Price of product dropped!"

    user = "theBotMail"
    msg['from'] = user
    #if you are doing it with gmail, you will need two way authentifcation and a app password (you can just create that right in gmail)
    password = "TheBotAppPassword"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


checkPrice()
