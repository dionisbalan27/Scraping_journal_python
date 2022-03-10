import tracemalloc
import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup

i = 1
offset = 1
page = "first"
data = []

start1 = timeit.default_timer()  
tracemalloc.start()

db = mysql.connector.connect(
        host="localhost",user="root",passwd="",db="si_pp" )

 
cursor = db.cursor()
        
while page is not None:
    if offset <= 999999 :
    # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        start_akses = timeit.default_timer()
        url = "http://garuda.ristekbrin.go.id/journal/view/1254?page="+str(offset)+"&from=2015"
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent} 
        print(url)
        request = urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data_page = response.read() 
        end1 = timeit.default_timer()
        total1 = start1 - end1
        current1 = tracemalloc.get_traced_memory()
        current1 = current1[0] / 10**6
        print("waktu eksekusi pengkoneksian dgn database :",total1,"s")
        bsObj = BeautifulSoup(data_page, 'html5lib');
        start2 = timeit.default_timer()  
      
        page=bsObj.findAll("xmp", {"class": "subtitle-article"})

        result=bsObj.find("div", {"class": "ui segment padded article-box"})
        
        for item in result.findAll("div", {"class": "article-item"}):
            
            h1 = item.findAll("a")
            h3 = h1[0].find("xmp")
            title = h3.text
            detail = h1[0]["href"]
            
            author = ""
            
            for auth in item.findAll("a", {"class": "author-article"}):
                author = author+auth.text+"; "
            #title = h2.find("xmp").text
            #detail = h2['href']
            
            h2 = item.findAll("xmp", {"class": "subtitle-article"})
            tgl = ""
            if len(h2)>0:
                tgl = h2[0].text.split(":")[1]
            end2 = timeit.default_timer()
            total2 = end2 - start1
            current2 = tracemalloc.get_traced_memory()
            current2 = current2[0] / 10**6
            print("waktu eksekusi pengkoneksian dgn database :",total2,"s")  
            se = db.cursor()
            se.execute("SELECT Title FROM pbu_garuda" )
            rs = se.fetchall()
              
            out = list(itertools.chain(*rs))
            
            if title not in out :
                a = []
                a.append(title)
                a.append(author)
                a.append(detail)
                a.append(tgl)
                if a not in data :                 
                    data.append(tuple(a));
                    start3 = timeit.default_timer() 
         
                    sql = "INSERT INTO pbu_garuda(Title, Author, Detail, Date_Released) VALUES (%s, %s, %s, %s)" 
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="",db="si_pp" )
                    cursor = db.cursor()
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit();
                    end3 = timeit.default_timer()
                    total3 = start3 - end1
                    print("waktu eksekusi pengkoneksian dgn database :",total3,"s")
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
        offset = i
    else :
        print("end")
 #if offset == 1:
                      #  qw=[]
                      #  qw.append(total1)
                       # qw.append(total2);qw.append(total3)
                     #   c=[]
                      #  c.append(tuple(qw))
                      #  e=[];e.append(tuple(c))
                     #   qs=[]
                     #   qs.append(current1)
                     #   qs.append(current2);qs.append(current3)
                     #   d=[]
                     #   d.append(tuple(qs))
                     #   f=[];f.append(tuple(d))
   
            