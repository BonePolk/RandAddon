from MyImport import *

try:
    import requests
except:
    install('requests')
    
try:
    from bs4 import BeautifulSoup as BS
except:
    install('bs4')
    
from random import randint
import webbrowser

def parser(No = int(), Np = int(), Type = str()):
    texts = []
    pages = []
    
    if Np == 1:
    	site = "https://mcpehub.org/" + Type
    	site = requests.get(site)
    else:
    	site = "https://mcpehub.org/" + Type + "/page/" + str(Np)
    	site = requests.get(site)
    html = BS(site.content, "html.parser")
    i = 0
    if No > len(html.select("#dle-content > .col-xs-12 > .news-item > .news-item-info > h2")):
    	No = len(html.select("#dle-content > .col-xs-12 > .news-item > .news-item-info > h2"))
    for title in html.select("#dle-content > .col-xs-12 > .news-item > .news-item-info > h2"):
    	texts.append(title.text)
    	pages.append(html.select("#dle-content > .col-xs-12 > .news-item")[len(pages)].get("href"))
    page = requests.get(pages[No])
    html = BS(page.content, "html.parser")
    find = multiclassparse("download-item border-radius", html)
    links = []
    print("N°", No + 1, sep="")
    print(texts[No])
    print(pages[No])
    print("Способ скачивания:")
    print("  "+str(len(links)), "Не интересует", sep= ": ")
    
    links.append(pages[No])
    print("  "+str(len(links)), "Описание "+texts[No], sep= ": ")
    for way in find:
        name = way.select(".item-content > span")[0].text
        link = way.select(".item-content > .flex-sm > a")[0].get("href")
        links.append(link)
        print("  "+str(len(links)), name, sep= ": ")
        
    
    
    
   #find = find.select(".flex-sm")
    
    #print(find)
    inp = getintinputinrange(0,  len(links));
    if inp == 0:
        return ""
        
    webbrowser.open(links[inp-1])
    
    return ""
    
def getintinputinrange(start, end):
    inp = ""
    while not inp:
        try:
            inp = int(input("Введите число: "))
            
            if (inp == 0):
                return 0
            if (start > inp or inp > end):
                inp = 0
        except:
            inp = 0
            
    return inp
        
    
def multiclassparse(cl, html):
    new_h = []
    html = [html]
    for clt in cl.split(" "):
        cltd = "."+clt
        for h in html:
            new_h.extend(h.select(cltd))
            
        if (len(new_h) > 0):
            html = new_h
            new_h = []
    
    return html
    
def parserpages(Type = str()):
    site = 'https://mcpehub.org/' + Type
    site = requests.get(site)
    html = BS(site.content, "html.parser")
    find = html.select('.navigation > .flex > .flex > a')[2]
    return int(find.text)