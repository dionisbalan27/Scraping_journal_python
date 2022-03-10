import re
import tracemalloc
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

start1 = timeit.default_timer()  
tracemalloc.start()

db = mysql.connector.connect(
host="localhost",user="root",passwd="meliodasten10",db="scrape" )

cursor = db.cursor()

while page is not None:
    if offset < 10000 :
        # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        url = "https://www.sciencedirect.com/search?date=2015-2020&affiliations=diponegoro%20university&show=100&offset="+str(offset)
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
    
        request = urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data_page = response.read() # The data u needend1 = timeit.default_timer()
        end1 = timeit.default_timer()
        total1 = end1 - start1 
        current1 = tracemalloc.get_traced_memory()
        current1 = current1[0] / 10**6
        
        bsObj = BeautifulSoup(data_page, 'html5lib');
        start2 = timeit.default_timer()  

        page=bsObj.find("li", {"class":"next-link"})
    

        result=bsObj.find("div", {"id": "srp-results-list"})

        for item in result.findAll('li', {"class":"ResultItem"}):
            judul = item.find("h2").find("span").find("a");
            h3 = item.find("div", {"class": "SubType"})
            tahun=h3.findAll("span")
            item2 = item.find("ol", {"class": "Authors"})
    
        #     print(item2.prettify())
    
            jud = judul.text;
            link = judul['href']
            tgl = tahun[3].text
            auth = item2.text
            end2 = timeit.default_timer()
            total2 = end2 - start1
            current2 = tracemalloc.get_traced_memory()
            current2 = current2[0] / 10**6
            se = db.cursor()
            se.execute("SELECT Title FROM tb_scd" )
            rs = se.fetchall()
              
            out = list(itertools.chain(*rs))
                
            if jud not in out :
                a = []
                a.append(jud);
                a.append(auth)
                a.append("https://www.sciencedirect.com"+link)
                a.append(tgl)
                data=[]
                data.append(tuple(a))
                start3 = timeit.default_timer() 
       
                sql = "INSERT INTO tb_scd(Title, Author, Detail, Date_Released) VALUES (%s, %s, %s, %s)" 
                
                for values in data:
                    cursor.execute(sql, values)
                    db.commit()
                end3 = timeit.default_timer()
                total3 = end3 - start1
                    
                current3 = tracemalloc.get_traced_memory()
                current3 = current3[0] / 10**6
                
                        
                db.close()
                
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
        offset = i*100
    else : 
        print(0)