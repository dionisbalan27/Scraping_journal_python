import re
import requests
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup
import mysql.connector

import tracemalloc

db = mysql.connector.connect(
    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )

cursor = db.cursor()

i = 0
offset = 0
page = "first"
data = []
 
while page is not None:
    if offset <= 9999999999 :
        tracemalloc.start()
        start = timeit.default_timer()
    # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        url = "https://scholar.google.co.id/scholar?start="+str(offset)+"&q=universitas+diponegoro&hl=id&as_sdt=0,5&as_ylo=2015&as_yhi=2020"
       
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent} 
        #print(url)
        request = urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data_page = response.read() # The data u need
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage connection is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    # author, title, years, cited, link download pdf, link detail
        stitle = timeit.default_timer()
        asdd = stitle - start;print("waktu eksekusi koneksi :",asdd,"s");
        start2 = timeit.default_timer()
        tracemalloc.start()
        bsObj = BeautifulSoup(data_page, 'html5lib'); bso = timeit.default_timer()
        asd = bso - start
        
        page=bsObj.find("div", {"class": "gs_ggs gs_fl"})

#     print(request)
        result=bsObj.find("div", {"id": "gs_res_ccl_mid"})
        
        for item in result.findAll('div', {"class":"gs_r gs_or gs_scl"}):
            h2 = item.find("h3").find("a")
            h3 = item.find("div", {"class": "gs_a"})
            
            if h2 is not None:
                judul = h2.text; 
                link = h2['href']
                auth = h3.text
                year = re.findall(r"\D(\d{4})\D", auth)
                
                
            se = db.cursor()
            se.execute("SELECT Judul FROM pbpu_gscholar" )
            rs = se.fetchall()
          
            out = []
            
            if judul not in out :
                s = "ejournal3.undip.ac.id"
                if s not in link :
                    a = []
                
                    a.append(judul);appj= timeit.default_timer();
                    asdf = appj - start
                    a.append(link)
                    a.append(auth.split("-",1)[0])
               
                    

                    if judul is not None:
                        data.append(tuple(a));
                        stitle2 = timeit.default_timer()
                        asdd2 = stitle2 - start2;print("waktu eksekusi scrap :",asdd2,"s");
                        current2, peak2 = tracemalloc.get_traced_memory()
                        print(f"Current memory usage scraping is {current2 / 10**6}MB; Peak was {peak2 / 10**6}MB")
                        
                        tracemalloc.start()
                        sql = "INSERT INTO pbpu_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                          
                        
                        current3, peak3 = tracemalloc.get_traced_memory()
                        print(f"Current memory usage db is {current3 / 10**6}MB; Peak was {peak3 / 10**6}MB")
                        
                         
                        
        i = (i+1)
        offset = i*10
else :
   
  print(0)
   
                