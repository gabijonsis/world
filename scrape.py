import pandas as pd
from bs4 import BeautifulSoup
import requests
# url = 'https://en.wikipedia.org/wiki/Latvia'


# url2='https://en.wikipedia.org/wiki/' + 'Equatorial Guinea'

# response = requests.get(url2)
# print(response)

df=pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
df=df[0]
html = df.to_html()
text_file = open("table.html", "w", encoding="utf-8")
text_file.write(html)
text_file.close()


# df=pd.read_html(url)
# df=df[0]

# df.to_excel('bandymukas.xlsx')
# print(df)

# import csv
# with open('bandymukas.csv', 'r', encoding="utf8") as file:
#     reader = csv.reader(file)
#     list=[]
#     for row in reader:
#         list.append(row)
#     print(list)

# selected = 'Central African Republic'
# url="https://en.wikipedia.org/wiki/" + selected
# kazkas=[]
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# smth = soup.find('table', attrs={'class': 'vcard'})
# nzn = pd.read_html(str(smth))
# for item in nzn:
#     kazkas.append(item)

# print(nzn)