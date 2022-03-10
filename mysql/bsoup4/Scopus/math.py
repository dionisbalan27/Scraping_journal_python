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
    host="localhost",user="root",passwd="labkom",db="db_scopus" )
apppo = timeit.default_timer()
ppii = apppo - start
print("waktu eksekusi pengkoneksian dgn database :",ppii,"s")
# prepare a cursor object using cursor() method
cursor = db.cursor()
while page is not None:
    url = "https://www.scopus.com/results/results.uri?sort=plf-f&src=s&sid=c2e5b3c64741f81b825eb091ccc5b18a&sot=aff&sdt=aff&sl=34&s=AF-ID%2860069385%29+AND+SUBJAREA%28MATH%29&cl=t&offset="+str(offset)+"&origin=resultslist&ss=plf-f&ws=r-f&ps=r-f&cs=r-f&cc=10&txGid=f3f0bb22111356f24bedcaa0830bc332"
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
    page=bsObj.find("span", {"class": "ico-navigate-right"})

    print(url)
    result=bsObj.find("table", {"id": "srchResultsList"})
    
    for item in result.findAll('tr', {"class": "searchArea"}):
        h2 = item.find("td", {"data-type": "docTitle"}).find("a")
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
        judul = h2.text
        link = h2['href']
        auth = h3.text
        tgl = h4.text
        sou = h5.text
        
        
        #rint("judul :",judul)
        #print("detail : ",link)
        #print("auth: ",auth)
        #print("tgl: ",tgl)
        #print("source: ",sou)
        #print("linsource: ",lins)
        #print("cited by: ",cit)

        se = db.cursor()
        se.execute("SELECT Title FROM mathematics" )
        rs = se.fetchall()
        out = list(itertools.chain(*rs))
        
        if judul not in out :
            c = []
            c.append(judul)
            c.append(auth)
            c.append(link)
            c.append(tgl)
            c.append(sou)
            c.append("https://www.scopus.com"+lins)
            c.append(cit)

            data3.append(tuple(c))
            print("jumlah data mathematics =" + str(len(data3)))
            
            if i == 1:
                
                    d = []
                    d.append(ppii)
                    d.append(asdd);c.append(asd)
                    d.append(apog)
                    d.append(asdg)
                    
    i = (i+1)
    offset = i

else :
     
     
     sql = "INSERT INTO mathematics(Title, Author, Detail, Date_Released, Source, Link_Source, Cited_By) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
     print(len(datae))   
            # try:
     i = 0
     for values in datae:
         cursor.execute(sql, values)
         db.commit()
     alpd = timeit.default_timer();sdg = alpd - start;print(sdg)
     c.insert(5,sdg);poll=c[0:6]
     print(poll)
    
            
     db.close()