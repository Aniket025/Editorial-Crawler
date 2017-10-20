import requests
from bs4 import BeautifulSoup

def singleitem(itemurl):
 sourcecode = requests.get(itemurl).text
 soup = BeautifulSoup(sourcecode, "html.parser")

 for link in soup.findAll("div", {"class":"panel-body"}):
  print(link.text)

url = "http://www.netmeds.com/prescriptions"
sourcecode = requests.get(url)
text = sourcecode.text
soup = BeautifulSoup(text,"html.parser")

for link in soup.findAll('div', {"class":"four-col"}):
    print(link.text)
    for item in link.findAll('a'):
        href = "http://www.netmeds.com" + item.get('href')
        print(href)
        singleitem(href)