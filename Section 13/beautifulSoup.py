import bs4
import requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceblock_ourprice')
    return elems[0].text.strip()

price = getAmazonPrice('http://www.amazon.com/Nordic-Games-Darksiders-Replica-Chaoseater-Sword/dp/B002LNHHHS/ref=sr_1_1?s=videogames&ie=UTF8&qid=1456798862&sr=1-1&keywords=video+games')