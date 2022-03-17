import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup

sql = """INSERT INTO pbpu_ipr(Nama, Jurusan, Nidn, Judul, Id_ipr, Tahun_Permohonan, 
Kategori, Patent_Holder, inventor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text;
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Sipil");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Perkapalan");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Komputer");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.PWK");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Arsitektur");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Geologi");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Kimia");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Geodesi");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Mesin");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Industri");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
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
        page1="ar";i=1;ofset=1;f=[]
        while page1 is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=ipr"
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
                ht = hi.find("h4", {"class": "uk-text-primary"}).text; 
                db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                se = db.cursor();se.execute("SELECT Judul FROM pbp_ipr" )
                rs = se.fetchall()
                out = list(itertools.chain(*rs))
                if ht not in out :
                    h3 = h2[0].find("span", {"class": "uk-text-success"}).text; 
                    h4 = h2[1].findAll("span", {"class": "uk-text-success"})
                    ho = h4[0].text
                    hth = h4[1].text
                    h5 = h2[2].find("span", {"class": "uk-text-success"}).text
                    he = h5[49:]
                    h6 = h2[3].find("ul", {"class": "uk-list"}).find("li").find("a")
                    h7 = h6.text;h8 = h6['href']
                    title = ht
                    ID = h3
                    tahun = hth
                    holder = he
                    inventor = h7
                    link_inventor = "https://sinta.ristekbrin.go.id"+h8
                    c=[]
                    c.append(ax)
                    c.append("(S1)T.Elektro");c.append(nidn.strip())
                    c.append(title)
                    c.append(ID);c.append(tahun);c.append(ho)
                    c.append(holder);c.append(inventor)
                    data=[]
                    data.append(tuple(c))
                    start = timeit.default_timer()
                        
                    db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                    cursor = db.cursor()
                    
                    for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                          
                                
                    db.close() 
            i=i+1
            ofset=i
    o=o+1
    offset=o
