import urllib2
from bs4 import BeautifulSoup

# url = "https://webscraper.io/test-sites/e-commerce/scroll"
url = "https://es.wikipedia.org/wiki/Elecciones_presidenciales_de_Eslovenia_de_2022"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, features="html.parser")

# print soup.find('div', {'id': 'layout-footer'})
# print soup.find('div', {'id': 'mw-content-text'})
print soup.find('span', {'id': 'Sistema_electoral'})

if __name__ == '__main__':
    pass
