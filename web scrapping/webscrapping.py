import pandas as pd
import requests
from bs4 import BeautifulSoup
webpage=requests.get('https://lol.fandom.com/wiki/LPL/2022_Season/Spring_Season').text
soup=BeautifulSoup(webpage,'lxml')
print(soup.prettify())#will give us tha properly arranged html code
