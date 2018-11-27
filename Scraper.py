import urllib2
from bs4 import BeautifulSoup
quote_page = v2.aitapps.iu.edu/INPARK_LotCount_V1_Online/IN 
page = urllib2.urlopen(quote_page) 
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'Row Fluid'})
name = name_box.text.strip()
print(name)
