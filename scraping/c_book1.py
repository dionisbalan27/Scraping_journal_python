import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
import itertools
from bs4 import BeautifulSoup

global sql
sql = "INSERT INTO pbpu_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
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
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
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
                title=ht;print(title)
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
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1    
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=36201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text;print(title) 
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
                    isbn = h3;print(isbn)
                    Aut = h4.replace('\n', '').strip();print(Aut)
                    publisher = h5;print(publisher)
                    pld = h6;print(pld)
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Perkapalan");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
                i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=56201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Komputer");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )   
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=35201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.PWK");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=23201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Arsitektur");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )   
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=34201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Geologi");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=24201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Kimia");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=29201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Geodesi");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=21201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Mesin");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=26201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Industri");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"
li=[];f=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=20201&view=authors&sort=year2'
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent} 
    request = urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data_page = response.read() 
    bsObj = BeautifulSoup(data_page, 'html5lib'); 
    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        page1="ar";i=1;f=[];ofset=1
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
                title = hi.find("h4", {"class": "uk-text-primary"}).text; 
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
                    c.append("(S1)T.Elektro");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
                    db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
