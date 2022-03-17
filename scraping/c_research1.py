import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup


sql = "INSERT INTO pbp_research(Nama, Jurusan, Nidn, A, B, C, D, E, F) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" 

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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Sipil");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Perkapalan");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Komputer");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.PWK");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Arsitektur");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Geologi");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Kimia");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Geodesi");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Mesin");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Industri");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
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
        page="ar";i=1;f=[];ofset=1
        while page is not None:
            ur="https://sinta.ristekbrin.go.id/authors/detail?page="+str(ofset)+"&id="+zc.strip()+"&view=research"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib'); 
            page= bsObj.find("dl", {"class": "uk-description-list-line"});
            for items in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
                    h5=items.find("dt").find("a").text;
                    db = mysql.connector.connect(
                    host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                    se = db.cursor();se.execute("SELECT A FROM pbp_research" )
                    rs = se.fetchall()
                    out = list(itertools.chain(*rs))
                    if h5 not in out :
                        h6=items.findAll("dd");h7=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[1].strip();
                        f1=h6[0].text.strip().split("\xa0\xa0 | \xa0\xa0")[0];f2=f1+","+" "+h7
                        h8=h6[1].text.strip().split("\n");
                        po=0;g1=""
                        if len(h8) == 1 :
                            for po in range(len(h8)):
                                g1=h8[po].strip().replace(",","");
                                po+=1
                        else :
                            for po in range(len(h8)):
                                g1=g1+" "+h8[po].strip();
                                po+=1
                        g2=g1.strip();h11=h6[3].text.strip();
                        h10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[0].strip();
                        q10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[1].split("\xa0\xa0\xa0\n")[1].strip();
                        w10=h6[2].text.strip().split("\xa0\xa0\xa0  \n")[0].strip();
                        t1=h10+" "+q10+" "+w10;
                        h9=bsObj.find("td", {"class": "uk-text-center"}).text;print(h9)
                        c=[]
                        c.append(ax)
                        c.append("(S1)T.Elektro");c.append(nidn.strip())
                        c.append(h5)
                        c.append(f2);c.append(g2)
                        c.append(t1)
                        c.append(h9);c.append(h11)
                        data=[]
                        data.append(tuple(c))
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
    
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        alpd = timeit.default_timer()
                        
                                
                        db.close()
            i=i+1
            ofset=i
    o=o+1
    offset=o