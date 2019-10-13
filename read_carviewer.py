from bs4 import BeautifulSoup

with open ("carviewer") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#print(soup.tr)
rows = soup.findAll("tr")
for row in rows:
    datalist = []
    cols = row.findAll("td")
    for col in cols:
        datalist.append(col.text)
    print(datalist)