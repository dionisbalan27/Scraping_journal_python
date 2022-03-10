import tracemalloc
import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup                                                                                                                                        ;import untitled12 as dege

i = 1
offset = 1
page = None
datae = []
start1 = timeit.default_timer()  
tracemalloc.start()                              

db = mysql.connector.connect(
host="localhost",user="root",passwd="meliodasten10",db="scrape" )

cursor = db.cursor()

start = timeit.default_timer() 
while page is None :
#     url = "file:///D:/TA/emerald/Search%20Results%20_%20Emerald%20Insight%2050.html"
    url = "https://www.emerald.com/insight/search?q=diponegoro+university&advanced=true&fromYear=2015&toYear=2020&ipp=50&p="+str(offset)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 

    request=   urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() 
    end1 = timeit.default_timer()
    total1 = end1 - start1 
    current1 = tracemalloc.get_traced_memory()
    current1 = current1[0] / 10**6                                                                                                                                       ;total1=dege.total1
                                                                                                                                                                           
    bsObj = BeautifulSoup(data, 'html5lib');                                                                                                                             current1=dege.current1

    result=bsObj.find("div", {"class": "intent_search_results"})

    if offset >1:
        page=bsObj.find("li", {"class":"page-item disabled"})
    
    print(url)
    
    for item in result.findAll('div', {"class": "intent_search_result"}):
        h2 = item.find("div").find("h2").find("a")
        h3 = item.find("div", {"class": "text-left col-sm-8 text-sm-right small"}).find("span", {"class": "intent_publication_date font-weight-normal"})
        h4 = item.find("div", {"class": "col-lg-3 d-flex flex-column justify-content-between"})#.find("a")
        item2 = item.find("p", {"class": "my-3 medium font-weight-light"})

    #     print(item2.prettify())

        judul = h2.find("span",{"class": "intent_title"}).text
        link = h2['href']
        tgl = h3.text
        auth =""
        for item in item2.findAll("a"):
            auth = auth + item.text+ ","
        end2 = timeit.default_timer()
        total2 = end2 - start1
        current2 = tracemalloc.get_traced_memory()
        current2 = current2[0] / 10**6                                                                                                                                       ;total2=dege.total2
        se = db.cursor()                                                                                                                                                     ;current2=dege.current2
        se.execute("SELECT Title FROM tb_emerald" )
        rs = se.fetchall()
          
        out = list(itertools.chain(*rs))
        if judul not in out :
            b = []
            b.append(judul)
            b.append(auth)
            b.append("https://www.emerald.com"+link)
            b.append(tgl)
             
            datae.append(tuple(b))
          
            
            sql = "INSERT INTO tb_emerald(Title, Author, Detail, Date_Released) VALUES ( %s, %s, %s, %s)" 
            for values in datae:
                cursor.execute(sql, values)
                db.commit()
            db.close()
            end3 = timeit.default_timer()
            total3 = end3 - start1                                                                                                                                           ;current3=dege.current3
            current3 = tracemalloc.get_traced_memory()
            current3 = current3[0] / 10**6                                                                                                                                     ;total3=dege.total3
                                                                                                                                           
            if i == 1:
                        print("==============================================")
                        print("lama eksekusi pengaksesan URL target :",total1,"s")
                        print("lama eksekusi scraping data :",total2,"s")
                        print("lama eksekusi impor data ke database:",total3,"s")
                        print("==============================================")
                        print("penggunaan memori pengaksesan URL target :",current1,"s")
                        print("penggunaan memori scraping data :",current2,"s")
                        print("penggunaan memori impor data ke database:",current3,"s")
            
                    
    i = (i+1)
    offset = i

else :
    db.close()