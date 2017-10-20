import requests
from bs4 import BeautifulSoup
import datetime

class color:
 BOLD = '\033[1m'
 END = '\033[0m'

currentdatetime = datetime.datetime.now()

def crawler(url,divtype,classtype,otherdivtype,otherclass,typedate,datehead):
 sourcecode = requests.get(url).text
 soup = BeautifulSoup(sourcecode, "html.parser")

 for link in soup.findAll(divtype,{ "class": classtype}):
    print(color.BOLD + link.text + color.END)
    for item in link.findAll('a'):
        href = item.get('href')
        singleitem(href,otherdivtype,otherclass)
        extractdate(href,typedate,datehead)

def singleitem(itemurl,otherdivtype,otherclass):
 sourcecode = requests.get(itemurl).text
 soup = BeautifulSoup(sourcecode, "html.parser")

 for link in soup.findAll(otherdivtype, {"class":otherclass}):
  print(link.text)

def extractdate(geturl,typedate,datehead):
  sourcecode = requests.get(geturl).text
  soup = BeautifulSoup(sourcecode, "html.parser")
  for link in soup.findAll( typedate, {"class": datehead}):
   print(link.text)

print(currentdatetime)

print("****  1 :  Timesofindia    *****  ")
crawler("http://blogs.timesofindia.indiatimes.com/toi-editorials/","h2","media-heading",'div',"content","span","date")

print("****  2 :  Economictimes   ***** ")
crawler("http://blogs.economictimes.indiatimes.com/et-editorials/","h2","media-heading",'div',"content","span","date")

print("****  3 :    Nytimes       ***** ")
crawler("https://www.nytimes.com/pages/opinion/index.html","div","story",'p',"story-body-text story-content","time","dateline")

print("****  4 :  Thetelegraph    *****")
crawler("http://thetelegraph.com/category/editorials/","div","item-wrap clearfix",'article',"","time","entry-date")

print("****  5 : Newindianexpress *****")
crawler("http://www.newindianexpress.com/Opinions/editorials","div","section_editorial",'div',"page","p","ArticlePublish")

