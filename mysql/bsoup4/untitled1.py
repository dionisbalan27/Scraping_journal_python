from selenium import webdriver
import urllib.request
from bs4 import BeautifulSoup
import re
import requests

page = "first"
page1 = "first"
li=[];f=[]
dblst={"nidn":1, "documentsgs":1}
url='https://sinta.ristekbrin.go.id/departments/detail?afil=6&id=20201&view=authors'
print(url)
chrome_path = r"C:\Users\Asus\Documents\Python Scripts\selenium\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get(url);
data_page = driver.page_source
bsObj = BeautifulSoup(data_page, 'html5lib');
for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
    h1=item.find("dt").find("a")['href'];
    h2=re.findall("\d{1,}", h1);h3=str(h2).split("'").pop(1)
    h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",h3.strip(),"-------------------------");
    dblst={"nidn":1, "documentsgs":1}
    ofset=1;i=1
    dblst["id"]=h3.strip();print(dblst);li.append(dblst)
    print("----------------------gscholar nidn :"+h3.strip()+"------------------------------------------------------")
    while page1 is not None:
        ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+h3.strip()+"&view=documentsgs"
        page1 = None
    page="a"
    while page is not None:
        url="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+h3.strip()+"&view=research"
        print(url)
        driver.get(url);
        data_page = driver.page_source
        bsObj = BeautifulSoup(data_page, 'html5lib');
        page= bsObj.find("dl", {"class": "uk-description-list-line"});
        for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                h5=items.find("dt").find("a").text;
                h6=items.findAll("dd");h7=h6[0].text.strip();
                h8=h6[1].text.strip();h10=h6[2].text.strip();
                h11=h6[3].text.strip();
                e={"a":1, "b":2, "c":3, "d":3, "e":3, "f":3};
                e["a"]=h5;e["b"]=h7;e["c"]=h8;e["d"]=h10;e["e"]=h11;
                f.append(e);print(f)
        i=i+1
        ofset=i