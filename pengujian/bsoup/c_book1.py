import re
import tracemalloc
import requests
import mysql.connector
import urllib.request

import timeit
import itertools
from bs4 import BeautifulSoup

global sql
sql = "INSERT INTO pbpu_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
    
start1 = timeit.default_timer()  
tracemalloc.start()     
           
pagem = "first"
data=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=22201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    end1 = timeit.default_timer()
    total1 = end1 - start1 
    current1 = tracemalloc.get_traced_memory()
    current1 = current1[0] / 10**6

    bsObj = BeautifulSoup(data_page, 'html5lib');

    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        end2 = timeit.default_timer()
        total2 = end2 - start1
        current2 = tracemalloc.get_traced_memory()
        current2 = current2[0] / 10**6
   
        page1="ar";i=1;f=[];ofset=1;print(zc.strip())
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=book"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page1= bsObj.find("dl", {"class": "uk-description-list-line bookmeta"})
            for item in bsObj.findAll("dl", {"class": "uk-description-list-line bookmeta"}):
                h2 = item.findAll("dd")
                hi = item.find("dt")  
                ht = hi.find("h4", {"class": "uk-text-primary"}).text;title = ht
                title=ht;
                db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                se = db.cursor()
                se.execute("SELECT Judul FROM pbp_book" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if title not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].find("span", {"class": "uk-text-success"}).text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    h6 = item.find("dd", {"class": "uk-text-success"}).text
                    isbn = h3
                    Aut = h4.replace('\n', '').strip()
                    publisher = h5
                    pld = h6
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Sipil");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld);print(isbn)
                    data=[]
                    data.append(tuple(c))
                    start3 = timeit.default_timer() 
         
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
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
                        
            i=i+1    
            ofset=i
    o=o+1
    offset=o
