import re
import requests
import mysql.connector
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup

i = 1
offset = 1
page = None
datae = []; 
c=[]
start = timeit.default_timer()  

db = mysql.connector.connect(
host="localhost",user="root",passwd="meliodasten10",db="scrape" )
apppo = timeit.default_timer()
ppii = apppo - start
print("waktu eksekusi pengkoneksian dgn database :",ppii,"s")
        # prepare a cursor object using cursor() method
cursor = db.cursor()

start = timeit.default_timer() 
while page is None :

    if offset == 1 :
    #     url = "file:///D:/TA/emerald/Search%20Results%20_%20Emerald%20Insight%2050.html"
        url = "https://www.emerald.com/insight/search?q=diponegoro+university&advanced=true&fromYear=2015&toYear=2020&ipp=50&p="+str(offset)
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
    
        request=   urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read() # The data u need
        # author, title, years, cited, link download pdf, link detail
        bsObj = BeautifulSoup(data, 'html5lib'); bso = timeit.default_timer()
        asd = bso - start
        result=bsObj.find("div", {"class": "intent_search_results"})
    
        if offset >1:
            page=bsObj.find("li", {"class":"page-item disabled"})
        
        print(url)
        
        for item in result.findAll('div', {"class": "intent_search_result"}):
            h2 = item.find("div").find("h2").find("a")
            h3 = item.find("div", {"class": "text-left col-sm-8 text-sm-right small"}).find("span", {"class": "intent_publication_date font-weight-normal"})
            h4 = item.find("div", {"class": "col-lg-3 d-flex flex-column justify-content-between"})#.find("a")
            item2 = item.find("p", {"class": "my-3 medium font-weight-light"})
    
        #     print(item2.prettify())
    
            judul = h2.find("span",{"class": "intent_title"}).text; stitle = timeit.default_timer()
            asdd = stitle - start;print("waktu eksekusi title :",asdd,"s");
            link = h2['href']
            tgl = h3.text
            auth =""
            for item in item2.findAll("a"):
                auth = auth + item.text+ ","
    
            se = db.cursor()
            se.execute("SELECT Title FROM tb_emerald" )
            rs = se.fetchall()
              
            out = list(itertools.chain(*rs))
            if judul not in out :
                b = []
                b.append(judul);apod = timeit.default_timer();apog = apod - start;
                b.append(auth)
                b.append("https://www.emerald.com"+link)
                b.append(tgl)
              
        
                datae.append(tuple(b));appd = timeit.default_timer();asdg = appd - start;
                if offset == 1:
                    qw=[];er=[];ty=[];ui=[];op=[];
                    qw.append(ppii)
                    er.append(asdd);ty.append(asd)
                    ui.append(apog)
                    op.append(asdg)
                    c.append(tuple(qw))
                    c.append(tuple(er));c.append(tuple(ty))
                    c.append(tuple(ui))
                    c.append(tuple(op))
                    
            
               
                        
        i = (i+1)
        offset = i
    
    else :
         
         
         sql = "INSERT INTO tb_emerald(Title, Author, Detail, Date_Released) VALUES ( %s, %s, %s, %s)" 
         print(len(datae))   
                # try:
         i = 0
         for values in datae:
             cursor.execute(sql, values)
             db.commit()
         alpd = timeit.default_timer();sdg = alpd - start;print(sdg)
         poll=c[0:5];kl=[];kl.append(sdg);poll.append(tuple(kl))
         db = mysql.connector.connect(
         host="localhost",user="root",passwd="meliodasten10",db="waktu_eksekusi" )
         sql = "INSERT INTO scopus_engineering(a, b, c, d, e, f) VALUES(%d, %d, %d, %d, %d, %d)" 
         print(poll)   
         
        
                
         db.close()