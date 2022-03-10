import re
import requests
import urllib.request
import itertools
import timeit
from bs4 import BeautifulSoup
import mysql.connector


start = timeit.default_timer()
db = mysql.connector.connect(
    host="localhost",user="root",passwd="meliodasten10",db="scrape" )
dbpp = timeit.default_timer();asdpp = dbpp - start;
print("waktu eksekusi data pppp :",asdpp,"s")
cursor = db.cursor()

i = 0
offset = 0
page = "first"
data = []
 
while page is not None:
    if offset <= 9999999999 :
    # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        url = "https://scholar.google.co.id/scholar?start="+str(offset)+"&q=universitas+diponegoro&hl=id&as_sdt=0,5&as_ylo=2015&as_yhi=2020"
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent} 
        #print(url)
        request = urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data_page = response.read() # The data u need
    # author, title, years, cited, link download pdf, link detail
        bsObj = BeautifulSoup(data_page, 'html5lib'); bso = timeit.default_timer()
        asd = bso - start
        print("waktu eksekusi bso :",asd,"s")       

        page=bsObj.find("div", {"class": "gs_ggs gs_fl"})

#     print(request)
        result=bsObj.find("div", {"id": "gs_res_ccl_mid"})
        
        for item in result.findAll('div', {"class":"gs_r gs_or gs_scl"}):
            h2 = item.find("h3").find("a")
            h3 = item.find("div", {"class": "gs_a"})
            
            if h2 is not None:
                judul = h2.text; stitle = timeit.default_timer()
                asdd = stitle - start;print("waktu eksekusi title :",asdd,"s");
                link = h2['href']
                auth = h3.text
                year = re.findall(r"\D(\d{4})\D", auth)
                
                
            se = db.cursor()
            se.execute("SELECT Title FROM tb_gscholar" )
            rs = se.fetchall()
          
            out = list(itertools.chain(*rs))
            
            if judul not in out :
                s = "ejournal3.undip.ac.id"
                if s not in link :
                    a = []
                    a.append(judul);appj= timeit.default_timer();
                    asdf = appj - start
                    print("waktu eksekusi judul app :",asdf,"s")
                    a.append(auth.split("-",1)[0])
                    a.append(link)
                    if len(year)>0:
                        years = year
                        a.extend(years)
                    else :
                        a.append("no date published")
                    a.append("gscholar")
                    a.append("none")
                    a.append("none")
                    a.append("none")

                    if judul is not None:
                        data.append(tuple(a));
                        appd = timeit.default_timer();asdg = appd - start;
                        print("waktu eksekusi data app :",asdg,"s")    
                        print(len(data))
                                      
                        sql = "INSERT INTO tb_gscholar(Title, Author, Detail, Date_Released, Site_Journal, Source, Link_Source, Cited_By) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)" 
                          
                        # try:
                        i = 0
                        for values in data:
                            cursor.execute(sql, values)
                            db.commit();apppoo = timeit.default_timer();asloo = apppoo - start;
                            print("waktu eksekusi data mm :",asloo,"s")
     
                        data = []
        i = (i+1)
        offset = i*10
else :
        
   db.close()
                