
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
        bsObj = BeautifulSoup(data_page, 'html5lib'); end_akses = timeit.default_timer();total_akses = end_akses - start_akses;
        print("waktu eksekusi akses URL target :",total_akses,"s")
        start_scrap = timeit.default_timer()
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
                
            db = mysql.connector.connect(
            host="localhost",user="root",passwd="",db="si_pp" )
            se = db.cursor();se.execute("SELECT Title FROM pbu_garuda" )
            rs = se.fetchall()
            out = list(itertools.chain(*rs))
            
            if title not in out :
                a = []
                a.append(title)
                a.append(author)
                a.append(detail)
                a.append(tgl)
                if a not in data :   
                    data = []
                    data.append(tuple(a));
                    end_scrap = timeit.default_timer();total_scrap = end_scrap - start_scrap;
                    print("waktu eksekusi scrraping dan koleksi data :",total_scrap,"s")
                    start_db = timeit.default_timer(); 
                    sql = "INSERT INTO pbu_garuda(Title, Author, Detail, Date_Released) VALUES (%s, %s, %s, %s)" 
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="",db="si_pp" )
                    cursor = db.cursor()
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit();end_db = timeit.default_timer();total_db = end_db - start_db;
                    print("waktu eksekusi simpan data ke database server :",total_db,"s")
                    
                            
                    db.close()
                    
            
        i = (i+1)
        offset = i
    else :
        print("end")
        
   