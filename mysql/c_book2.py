import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
import itertools
from bs4 import BeautifulSoup

db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
apppo = timeit.default_timer()

cursor = db.cursor()
pagem = "first"
data=[]
offset=1;o=1
while pagem is not None:
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=24001&view=authors&sort=year2'
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text;title = ht
                title=ht
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
                    c.append("(S3)T.Kimia");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                                                            
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=20101&view=authors&sort=year2'
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
                se = db.cursor();se.execute("SELECT Judul FROM pbp_book" )
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
                    c.append("(S2)T.Elektro");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=26101&view=authors&sort=year2'
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
                    c.append("(S2)Teknik Dan Manajemen Industri");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=21001&view=authors&sort=year2'
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
                    c.append("(S3)T.Mesin");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=22001&view=authors&sort=year2'
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
                    c.append("(S3)Ilmu T.Sipil");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=21101&view=authors&sort=year2'
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
                    c.append("(S2)T.Mesin");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=35401&view=authors&sort=year2'
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
                    c.append("(D3)T.Perencanaan dan Kota K. Pekalongan");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=22313&view=authors&sort=year2'
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
                    c.append("(D4)T.Infrastruktur Sipil dan Perancangan Arsitek");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                    
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=22101&view=authors&sort=year2'
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
                    c.append("(S2)T.Sipil");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=20401&view=authors&sort=year2'
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
                    c.append("(D4)T.Elektronika");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
    url='https://sinta.ristekbrin.go.id/departments/detail?page='+str(offset)+'&afil=6&id=20305&view=authors&sort=year2'
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
                    c.append("(D4)T.Listrik Industri");c.append(nidn.strip())
                    c.append(title)
                    c.append(isbn);c.append(Aut);c.append(publisher)
                    c.append(pld)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
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
