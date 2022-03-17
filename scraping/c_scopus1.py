import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup

db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
apppo = timeit.default_timer()


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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Sipil");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Perkapalan");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Komputer");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.PWK");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Arsitektur");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Geologi");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Kimia");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Geodesi");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Mesin");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Industri");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
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
        page = "first"
        page1=None;i=1;ofset=1
        while page1 is None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=documentsscopus"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            if ofset == 1 :
               page1=None
            else :
               page1= bsObj.find("li", {"class": "uk-disabled"})
            for ol in bsObj.find("tbody").findAll("tr") :
                    items=ol.find("dl", {"class": "uk-description-list-line"})
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
        host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor()
                    se.execute("SELECT Judul FROM pbp_scopus" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        sso=ol.findAll("td", {"class": "index-val uk-text-center"})[1].text;print(sso)
                        c1=items.find("dt").find("a")['href'];
                        h6=items.find("dd").text.strip().split("\n");h7=h6.pop(1).strip()
                        h8=h6.pop(0);h9=h8+" "+h7
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Elektro");c.append(nidn.strip())
                        c.append(h5)
                        c.append(h9);c.append(c1);c.append(sso)
                        data=[]
                        data.append(tuple(c))
                        start = timeit.default_timer()
                        
                        db = mysql.connector.connect(
                                host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        sql = "INSERT INTO pbp_scopus(Nama, Jurusan, Nidn, Judul, Link_Judul, Index_By, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                                          
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o
