import re
import tracemalloc
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup

start1 = timeit.default_timer()  
tracemalloc.start() 
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
    end1 = timeit.default_timer()
    total1 = end1 - start1 
    current1 = tracemalloc.get_traced_memory()
    current1 = current1[0] / 10**6
    bsObj = BeautifulSoup(data_page, 'html5lib');
    start2 = timeit.default_timer()  

    pagem=bsObj.find("dl", {"class": "uk-description-list-line"}) 
    for item in bsObj.findAll("dl", {"class": "uk-description-list-line"}) :
        h1=item.find("dt").find("a")['href'];ax=item.find("dt").find("a").text
        h2=re.findall("\d{1,}", h1);zc=str(h2).split("'").pop(1)
        h4=item.findAll("dd");nidn=h4[1].text.split(":").pop(1);print("------------",nidn,"-------------------------");
        end2 = timeit.default_timer()
        total2 = end2 - start1
        current2 = tracemalloc.get_traced_memory()
        current2 = current2[0] / 10**6
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
                        start3 = timeit.default_timer() 
                      
                        db = mysql.connector.connect(
                            host="localhost",user="root",passwd="meliodasten10",db="si_pp" )
                        
                        cursor = db.cursor()
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit()
                        end3 = timeit.default_timer()
                        total3 = end3 - start1
                        
                        current3 = tracemalloc.get_traced_memory()
                        current3 = current3[0] / 10**6
                                                    
                        db.close()
                        if i == 1:
                            print("==============================================")
                            print("lama eksekusi pengaksesan URL target :",total1,"s")
                            print("lama eksekusi scraping data :",total2,"s")
                            print("lama eksekusi impor data ke database:",total3,"s")
                            print("==============================================")
                            print("penggunaan memori pengaksesan URL target :",current1,"s")
                            print("penggunaan memori scraping data :",current2,"s")
                            print("penggunaan memori impor data ke database:",current3,"s")
            i=i+1
            ofset=i
    o=o+1
    offset=o
