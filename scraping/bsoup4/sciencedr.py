import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup

i = 0
offset = 0
page = "first"
data= [];c=[]
judul = []

start = timeit.default_timer()  

db = mysql.connector.connect(
host="localhost",user="root",passwd="meliodasten10",db="scrape" )
apppo = timeit.default_timer()
ppii = apppo - start
print("waktu eksekusi pengkoneksian dgn database :",ppii,"s")
        # prepare a cursor object using cursor() method
cursor = db.cursor()

while page is not None:
    if offset < 10000 :
        # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        url = "https://www.sciencedirect.com/search?date=2015-2020&affiliations=diponegoro%20university&show=100&offset="+str(offset)
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
    
        request = urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data_page = response.read() # The data u need
        # author, title, years, cited, link download pdf, link detail
        bsObj = BeautifulSoup(data_page, 'html5lib'); bso = timeit.default_timer()
        asd = bso - start
        page=bsObj.find("li", {"class":"next-link"})
    
        print(url)
        result=bsObj.find("div", {"id": "srp-results-list"})
        print(result)
        for item in result.findAll('li', {"class":"ResultItem"}):
            judul = item.find("h2").find("span").find("a");
            h3 = item.find("div", {"class": "SubType"})
            tahun=h3.findAll("span")
            item2 = item.find("ol", {"class": "Authors"})
    
        #     print(item2.prettify())
    
            jud = judul.text;stitle = timeit.default_timer()
            asdd = stitle - start;print("waktu eksekusi title :",asdd,"s");
            link = judul['href']
            tgl = tahun[3].text
            auth = item2.text
         
            se = db.cursor()
            se.execute("SELECT Title FROM tb_scd" )
            rs = se.fetchall()
              
            out = list(itertools.chain(*rs))
                
            if jud not in out :
                a = []
                a.append(jud);apod = timeit.default_timer();apog = apod - start;
                a.append(auth)
                a.append("https://www.sciencedirect.com"+link)
                a.append(tgl)
                  
                data.append(tuple(a));appd = timeit.default_timer();asdg = appd - start;
                print(len(data))
                if i == 0:
                    
                    c.append(ppii);c.append(asd)
                    c.append(asdd)
                    c.append(apog)
                    c.append(asdg)
                
        i = (i+1)
        offset = i*100
    else : 
        sql = "INSERT INTO tb_scd(Title, Author, Detail, Date_Released) VALUES (%s, %s, %s, %s)" 
                
        for values in data:
            cursor.execute(sql, values)
            db.commit()
        alpd = timeit.default_timer();sdg = alpd - start;print(sdg)
        c.insert(5,sdg);poll=c[0:6]
        print(poll)
        
                
        db.close()