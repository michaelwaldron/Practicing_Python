# -*- coding: utf-8 -*-
"""
Practice Python Exercise 17

Print a list of all article titles on New York Times homepage

"""

# Package to get HTML script
import requests
# Package to parse HTML script
from bs4 import BeautifulSoup

# Use requests to get HTML script
url = 'https://www.newyorktimes.com/'
r = requests.get(url)
r_html = r.text

# Load HTML script into Soup
soup = BeautifulSoup(r_html, "lxml")

# Print article titles
headlines = soup.find_all(class_= "story-heading")
for headline in headlines:
    if headline.a:
        print(headline.a.text.replace("\n"," ").strip())
    else:
        print(headline.contents[0].strip())
"""
# Store and print article titles
titles = []
headlines = soup.find_all(class_= "story-heading")
for headline in headlines:
    if headline.a:
        titles.append(headline.a.text.replace("\n"," ").strip())
    else:
        titles.append(headline.contents[0].strip())
print(titles)
"""