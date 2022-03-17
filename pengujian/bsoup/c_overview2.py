import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup
          
global password,database
password=""
database="si_pp"    
pagem = "first"
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
        print(ax);db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Kimia")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database )
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1;offset=o          
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database )
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Elektro")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database )
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database )
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Industri")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database )
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1;offset=o          
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Mesin")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database)
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Sipil")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database )
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1;offset=o          
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Mesin")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database )
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr")
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    bs=ite.find("tbody").findAll("tr");
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Perencanaan Wilayah dan Kota")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database)
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Infrastruktur Sipil dan Perancangan Arsitek")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database)
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Sipil")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database)
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
            a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Elektronika")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database)
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
pagem = "first"
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
        db = mysql.connector.connect(
        host="localhost",user="root",passwd=password,db=database)
        se = db.cursor();se.execute("SELECT Nama FROM pbp_overview" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        if ax not in out :
            h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1).strip()
            h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
            dblst={"nidn":1, "documentsgs":1, "documentsscp":1, "documentswos":1, "ipr":1, "book":1, "research":1 }
            ofset=1;i=1
            dblst["nidn"]=nidn.strip()
            ur="https://sinta.ristekbrin.go.id/authors/detail?id="+zc+"&view=overview"
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent} 
            request = urllib.request.Request(ur,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data_page = response.read() 
            bsObj = BeautifulSoup(data_page, 'html5lib');
            mu= bsObj.find("div", {"class": "uk-width-large-4-10 default-stat uk-vertical-align uk-grid"})
            img=mu.find("div", {"class": "uk-width-2-10"}).find("img", {"class": "author-photo-normal uk-align-left"})["src"]
            page= bsObj.find("div", {"class": "au-data uk-vertical-align-middle uk-width-8-10"})
            NR=bsObj.findAll("div", {"class": "stat2-val"})[5].text;print(zc)
            NR3=bsObj.findAll("div", {"class": "stat2-val"})[6].text;
            AR=bsObj.findAll("div", {"class": "stat2-val"})[8].text;
            AR3=bsObj.findAll("div", {"class": "stat2-val"})[9].text;
            flag=page.find("div", {"class": "au-flag"}).text
            for ite in bsObj.findAll("table", {"class": "uk-table top5-paper"}):
                bs=ite.find("tbody").findAll("tr");
                if len(bs)<5 :
                    link_judul1, link_judul2, link_judul3, link_judul4, link_judul5 ="none","none","none","none","none"
                    index_by1, index_by2, index_by3, index_by4, index_by5="none","none","none","none","none"
                    judul1, judul2, judul3, judul4, judul5="none","none","none","none","none"
                    citation1, citation2, citation3, citation4, citation5="none","none","none","none","none"
                else :
                    mo1=bs[0].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul1=mo1["href"];
                    index_by1=bs[0].find("dd", {"class": "indexed-by"})
                    index_by1="none" if index_by1 ==None else index_by1.text.strip();
                    judul1=mo1.text;
                    citation1=bs[0].find("td", {"class": "index-val uk-text-center"}).text
                    mo2=bs[1].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul2=mo2["href"];
                    index_by2=bs[1].find("dd", {"class": "indexed-by"})
                    index_by2="none" if index_by2 ==None else index_by2.text.strip();
                    judul2=mo2.text;
                    citation2=bs[1].find("td", {"class": "index-val uk-text-center"}).text
                    mo3=bs[2].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul3=mo3["href"];
                    index_by3=bs[2].find("dd", {"class": "indexed-by"})
                    index_by3="none" if index_by3 ==None else index_by3.text.strip();
                    judul3=mo3.text;
                    citation3=bs[2].find("td", {"class": "index-val uk-text-center"}).text
                    mo4=bs[3].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul4=mo4["href"];
                    index_by4=bs[3].find("dd", {"class": "indexed-by"})
                    index_by4="none" if index_by4 ==None else index_by4.text.strip();
                    judul4=mo4.text;
                    citation4=bs[3].find("td", {"class": "index-val uk-text-center"}).text
                    mo5=bs[4].find("dt", {"class": "uk-text-primary"}).find("a")
                    link_judul5=mo5["href"];
                    index_by5=bs[4].find("dd", {"class": "indexed-by"})
                    index_by5="none" if index_by5 ==None else index_by5.text.strip();
                    judul5=mo5.text;
                    citation5=bs[4].find("td", {"class": "index-val uk-text-center"}).text
                a=[]
            a.append(ax);a.append(nidn);a.append("Teknik Elektro")
            a.append(img);a.append(flag);a.append(zc);a.append(NR);a.append(NR3);a.append(AR);a.append(AR3)
            a.append(judul1);a.append(judul2);a.append(judul3);a.append(judul4);a.append(judul5);
            a.append(link_judul1);a.append(link_judul2);a.append(link_judul3);a.append(link_judul4);a.append(link_judul5);
            a.append(citation1);a.append(citation2);a.append(citation3);a.append(citation4);a.append(citation5);
            a.append(index_by1);a.append(index_by2);a.append(index_by3);a.append(index_by4);a.append(index_by5);
            data=[]
            data.append(tuple(a))
            db = mysql.connector.connect(
            host="localhost",user="root",passwd=password,db=database)
            cursor = db.cursor()
            sql = """INSERT INTO pbp_overview(Nama, Nidn, Jurusan, image, Bandeira, Id_Sinta, National_Rank, 
            3YNational_Rank, Affiliation_Rank, 3YAffiliation_Rank, Judul1, Judul2, Judul3, 
            Judul4, Judul5, Link_Judul1, Link_Judul2, Link_Judul3, Link_Judul4, Link_Judul5,
             Citation1, Citation2, Citation3, Citation4, Citation5, Index_By1, Index_By2,
             Index_By3, Index_By4, Index_By5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            for values in data:
                        cursor.execute(sql, values)
                        db.commit()
                                  
            db.close()
    o=o+1          
    offset=o
