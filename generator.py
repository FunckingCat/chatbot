import requests
from lxml import etree
import lxml.html

def get_name(sex=10, count = 1):
    url = 'https://randomus.ru/name?type=0&sex=' + str(sex) + '&count=' + str(count)
    res = requests.get(url)
    tree = lxml.html.document_fromstring(res.text)
    name = tree.xpath('//*[@id="result_tiles"]/div/div/div/div/span/text()')
    return name
