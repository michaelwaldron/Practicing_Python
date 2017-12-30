# -*- coding: utf-8 -*-
"""
Practice Python Exercise 21

Take code from Exercise 17 but write text to file rather than print to screen.

"""

# Packages for HTML
import requests
from bs4 import BeautifulSoup

# Load and process HTML for headlines
url = 'https://www.newyorktimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "lxml")
headlines = soup.find_all(class_= "story-heading")

# Write headlines to file
file_name = str(input("Please enter a filename:")) + ".txt"
with open(file_name, 'w') as open_file:
    for headline in headlines:
        if headline.a:
            open_file.write(headline.a.text.replace("\n"," ").strip())
            open_file.write("\n")
        else:
            open_file.write(headline.contents[0].strip())
            open_file.write("\n")