import requests
import urllib.request
import mysql.connector
import itertools
from bs4 import BeautifulSoup
from http.cookiejar import CookieJar
import timeit

i = 0
offset = 0
page = "first"
data3 = []
c=[]
start = timeit.default_timer()  

db = mysql.connector.connect(
    host="localhost",user="root",passwd="",db="si_pp" )
apppo = timeit.default_timer()
ppii = apppo - start
print("waktu eksekusi pengkoneksian dgn database :",ppii,"s")
# prepare a cursor object using cursor() method
cursor = db.cursor()
if i == 0 :
    while page is not None:
        url = "https://www.scopus.com/results/results.uri?sort=plf-f&src=s&sid=e05c89ac3ed5b753518e625c32e7b395&sot=aff&sdt=aff&sl=34&s=AF-ID%2860069385%29+AND+SUBJAREA%28ENGI%29&cl=t&offset="+str(offset)+"&origin=resultslist&ss=plf-f&ws=r-f&ps=r-f&cs=r-f&cc=10&txGid=43f7bf04b20af3ad7b9fca1026917a77"
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
    
        request= urllib.request.Request(url,None,headers) #The assembled request
        cj = CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        response = opener.open(request)
        data_page = response.read() # The data u need
        # author, title, years, cited, link download pdf, link detail
        bsObj = BeautifulSoup(data_page, 'html5lib'); bso = timeit.default_timer()
        asd = bso - start
    
        page=bsObj.find("span", {"class": "ddmPubYr"})
        print(url)
        result=bsObj.find("table", {"id": "srchResultsList"})
        
        for item in result.findAll('tr', {"class": "searchArea"}):
            h2 = item.find("td", {"data-type": "docTitle"}).find("a")
            judul = h2.text; stitle = timeit.default_timer()
            asdd = stitle - start;print("waktu eksekusi title :",asdd,"s");
            db = mysql.connector.connect(
    host="localhost",user="root",passwd="",db="si_pp" )
            se = db.cursor()
            se.execute("SELECT Judul FROM pbpu_scopus" )
            rs = se.fetchall()
            out = list(itertools.chain(*rs))
            
            if judul not in out :
                h3 = item.find("span", {"class": "ddmAuthorList"})
                h4 = item.find("span", {"class": "ddmPubYr"})
                h5 = item.find("td", {"data-type": "source"})
                h6 = h5.find("a")
                lins = "None"
                if h6 is not None:
                    lins = h6['href']
                h7= item.findAll("td")
                h8= h7[4].find("a")
                cit = "0"
                if h8 is not None:
                    cit = h8.text
                
                link = h2['href']
                auth = h3.text
                tgl = h4.text
                sou = h5.text
                
                if judul not in out :
                    c = []
                    c.append("none")
                    c.append("none")
                    c.append("none")
                    c.append(judul);
                    
                    c.append(sou)
                    c.append(link)
                    c.append(cit)
                    data3=[]
                    data3.append(tuple(c));appd = timeit.default_timer();asdg = appd - start;
                    
                    db = mysql.connector.connect(
                     host="localhost",user="root",passwd="",db="si_pp" )
                    sql = "INSERT INTO pbpu_scopus(Nama, Jurusan, Nidn, Judul, Index_By, Link_Judul, Citation) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
                    print(len(data3))   
                            # try:
                   
                    cursor = db.cursor()
                    for values in data3:
                         cursor.execute(sql, values)
                         db.commit()
                    
                            
                    db.close()
                    
                    if i == 0:
                        d = []
                        
                    
                        
        i = (i+1)
        offset = i

else :
     print(0)
     
     