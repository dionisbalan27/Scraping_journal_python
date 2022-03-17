from selenium import webdriver 
from bs4 import BeautifulSoup
import mysql.connector
import re
import tracemalloc
import timeit
import itertools

i = 1
offset = 1
page = "first"
data = []


start1 = timeit.default_timer()  
tracemalloc.start() 
        
if offset <= 999999 :
    if offset <= 999999 :
    # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        chrome_path = r"D:\TA\mysql\pengujian\selenium\chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)
        driver.get("http://garuda.ristekbrin.go.id/journal/view/1254?page="+str(offset)+"&from=2015")
        end1 = timeit.default_timer()
        total1 = end1 - start1 
        current1 = tracemalloc.get_traced_memory()
        current1 = current1[0] / 10**6
        start2 = timeit.default_timer()  

        
        for res in driver.find_elements_by_xpath('//div[@class="article-item"]'):
            Title = res.find_element_by_xpath('a[@class="title-article"]/xmp').text
            Link_title = res.find_element_by_xpath('a[@class="title-article"]').get_attribute('href')
            print(Title); print(Link_title);
            auth2 = ""
            for auth1 in res.find_elements_by_xpath('a[@class="author-article"]'):
                auth2 = auth1.text + ";" + auth2
            author = auth2[0:-1]
            print(author)
            indeks = res.find_element_by_xpath('xmp[@class="subtitle-article"]').text
            downloadori =res.find_elements_by_xpath('p[@class="action-article"]/a[@class="title-citation"]')[0].get_attribute('href').strip()
            pdf = res.find_elements_by_xpath('p[@class="action-article"]/a[@class="title-citation"]')[1].get_attribute('href').strip()
            DOI = res.find_elements_by_xpath('p[@class="action-article"]/a[@class="title-citation"]')[2].text.replace("\r\n","").strip()
            end2 = timeit.default_timer()
            total2 = end2 - start1
            current2 = tracemalloc.get_traced_memory()
            current2 = current1[0] / 10**6
            a = []
            a.append(Title)
            a.append(author)
            a.append(Link_title)
           
            a.append("Desember 2019" )
            a.append(downloadori)
            a.append(pdf)
            a.append(DOI)
            data1=[]
                                                 
            data1.append(tuple(a));print(data1)
            start3 = timeit.default_timer() 
      
            db = mysql.connector.connect(
        host="localhost",user="root",passwd="",db="scrape" )
            cursor = db.cursor()
            sql = "INSERT INTO pbu_garuda(Title, Author, Detail, Date_Released) VALUES (%s, %s, %s, %s)" 
                    
            for values in data1:
                        cursor.execute(sql, values)
                        db.commit()
            end3 = timeit.default_timer()
            total3 = end3 - start1
            
            current3 = tracemalloc.get_traced_memory()
            current3 = current3[0] / 10**6
            db.close()  