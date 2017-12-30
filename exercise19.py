# -*- coding: utf-8 -*-
"""
Practice Python Exercise 19

Print to the screen the full text of the article on this website: 
<http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture>

Article is split between 4 pages - join the text.

"""

# Package to get HTML script
import requests
# Package to parse HTML script
from bs4 import BeautifulSoup

# Use requests to get HTML script
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

# Load HTML script into Soup
soup = BeautifulSoup(r_html, "lxml")

# Extract text with CSS selectors
introp = soup.find_all('div', {"class:", "dek"})
for item in introp:
    print(item.text)
mainp = soup.find_all('section', {"class:", "content-section"})
for item in mainp:
    print(item.text)