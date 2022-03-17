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
        driver.get("https://www.emerald.com/insight/search?q=diponegoro+university&advanced=true&fromYear=2015&toYear=2020&ipp=50&p=0")
        end1 = timeit.default_timer()
        total1 = end1 - start1 
        current1 = tracemalloc.get_traced_memory()
        current1 = current1[0] / 10**6
        start2 = timeit.default_timer()  
   
        for res in driver.find_elements_by_xpath('//div[@class="intent_search_result container card-shadow is-animated Search-item__wrapper"]'):
                title = res.find_element_by_xpath('.//div/h2[@class="h3 mt-0 mb-2"]/a/span[@class="intent_title"]').text
                link_title = res.find_element_by_xpath('.//div/h2[@class="h3 mt-0 mb-2"]/a').get_attribute('href')
                author=""
                for resauth in res.find_elements_by_xpath('.//p[@class="my-3 medium font-weight-light"]/a'):
                   author=author+resauth.text+", " 
                end2 = timeit.default_timer()
                total2 = end2 - start1
                current2 = tracemalloc.get_traced_memory()
                current2 = current1[0] / 10**6
                a = []
                a.append(title)
                a.append(author)
                a.append(link_title)
          
                               
                data1=[]
                                                     
                data1.append(tuple(a));print(data1)
        
                db = mysql.connector.connect(
            host="localhost",user="root",passwd="",db="scrape" )
                cursor = db.cursor()
                sql = "INSERT INTO pbp_research(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                        
                for values in data1:
                            cursor.execute(sql, values)
                            db.commit()
                end3 = timeit.default_timer()
                total3 = end3 - start1
                
                current3 = tracemalloc.get_traced_memory()
                current3 = current3[0] / 10**6
                db.close()  