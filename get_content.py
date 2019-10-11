# some test work to see if we can get content from a website.  Follow along from Andrew's videos. JR. 10.10.19

import requests
from bs4 import BeautifulSoup

page = requests.get("https://stackoverflow.com")

soup1 = BeautifulSoup(page.content, 'html.parser')

print(page)
print("---------------------------")
print(soup1.prettify())

