import requests
from bs4 import BeautifulSoup


xml_url = 'https://b2b.pwrs.ru/export_data/rest_spb_pish.xml'
r = requests.get(xml_url)
r.encoding = 'utf-8-sig'
xml = r.text
print('XML создан:')
print(type(xml))


soup = BeautifulSoup(xml, 'lxml-xml')
print(type(soup))
