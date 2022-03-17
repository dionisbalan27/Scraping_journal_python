import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup


pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1;print(zc.strip())
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;print(h5)
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Sipil");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                  
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1;print(zc.strip())
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;print(h5)
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Perkapalan");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1;print(zc.strip())
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;print(h5)
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Komputer");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.PWK");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Arsitektur");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Geologi");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Kimia");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Geodesi");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Mesin");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Industri");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
pagem = "first"

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
        dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
        ofset=1;i=1
        dblst["nidn"]=nidn.strip();page = "first"
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsgs"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            page= bsObj.find("dl", {"class": "uk-description-list-line"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_gscholar" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.findAll("dd");
                        if len(h6) != 2 :
                            h7=items.find('a')['href'];h8="none" 
                        else :
                            h7=h6[0].text;h8=h6[1].text.strip();
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Elektro");c.append(nidn.strip())
                        c.append(h5)
                        c.append(c1);c.append(h7);c.append(h8);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="scrape" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_gscholar(Nama, Jurusan, Nidn, Judul, Link_Judul, Author, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
