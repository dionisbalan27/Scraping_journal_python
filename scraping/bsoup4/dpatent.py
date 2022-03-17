
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
   
start = timeit.default_timer()  

db = mysql.connector.connect(
host="localhost",user="root",passwd="meliodasten10",db="scrape" )
apppo = timeit.default_timer()
ppii = apppo - start
print("waktu eksekusi pengkoneksian dgn database :",ppii,"s")
        # prepare a cursor object using cursor() method
cursor = db.cursor()

    
c=[]
while page is not None:
    if offset <= 999999999999:
    # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        url = "http://sinta.ristekbrin.go.id/haki?page="+str(offset)
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent} 
        request = urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data_page = response.read() ;print(url)
        bsObj = BeautifulSoup(data_page, 'html5lib'); bso = timeit.default_timer();
        poo = bso - start;
        print("waktu eksekusi koneksi driver :",poo,"s")
        
        page=bsObj.find("dl", {"class": "uk-description-list-line bookmeta"})
        
        result=bsObj.find("table", {"class": "uk-table"})
        
        for item in result.findAll("dl", {"class": "uk-description-list-line bookmeta"}):
            h2 = item.findAll("dd")
            hi = item.find("dt");startt = timeit.default_timer()    
            ht = hi.find("h4", {"class": "uk-text-primary"}).text; stitle = timeit.default_timer()
            app = stitle - startt;print("waktu eksekusi scarping title :",app,"s")
            h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
            h4 = h2[1].findAll("span", {"class": "uk-text-success"})
            hth = h4[1].text; tahun = timeit.default_timer()
            h5 = h2[2].find("span", {"class": "uk-text-success"}).text
            he = h5[49:]; holder = timeit.default_timer()
            h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
            h7 = h6.text; inventor = timeit.default_timer()
            h8 = h6['href']; link_inventor = timeit.default_timer()
            
            title = ht
            ID = h3
            tahun = hth
            holder = he
            inventor = h8
            link_inventor = h7
            
            se = db.cursor()
            se.execute("SELECT Title FROM tb_patent" )
            rs = se.fetchall()
          
            out = list(itertools.chain(*rs))
            
            if ht not in out :
                                       
                a = []
                a.append(ht);apj = timeit.default_timer();pop = apj - startt;
                print("waktu eksekusi append judul kedalam list a :",pop,"s")
                a.append(h3)
                a.append(hth)
                a.append(he)
                a.append(h7)
                a.append("http://sinta.ristekbrin.go.id"+h8)
                if a not in data :        
                    data.append(tuple(a));
                    apd = timeit.default_timer();
                    pok = apd - start;
                    print("waktu eksekusi memasukkan seluruh data scrape ke dalam list data :",pok,"s") 
                    print(len(data)) 
                    if i == 1:
                        c.append(ppii)
                        c.append(pok);c.append(poo)
                        c.append(app)
                        c.append(pop)
                                    
        i = (i+1)
        offset = i
    else :
       sql = "INSERT INTO tb_patent(Title, Author, Detail, Date_Released) VALUES (%s, %s, %s, %s)" 
                
       for values in data:
            cursor.execute(sql, values)
            db.commit()
       alpd = timeit.default_timer();sdg = alpd - start;print(sdg)
       c.insert(5,sdg);poll=c[0:6]
       print(poll)
        
                
       db.close()
        
        
        
        
                