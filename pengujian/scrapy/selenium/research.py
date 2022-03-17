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
        driver.get("https://sinta.ristekbrin.go.id/departments/detail?page=0&afil=6&id=22201&view=authors&sort=year2")
        end1 = timeit.default_timer()
        total1 = end1 - start1 
        current1 = tracemalloc.get_traced_memory()
        current1 = current1[0] / 10**6
        start2 = timeit.default_timer()  
 
        for res in driver.find_elements_by_xpath('//table[@class="uk-table"]/tbody/tr'):
            image = res.find_element_by_xpath('td/img[@class="author-photo-small uk-align-left"]').get_attribute('src').strip()
            title = res.find_element_by_xpath('td/dl[@class="uk-description-list-line"]/dt/a').text
            link_title = res.find_element_by_xpath('td/dl[@class="uk-description-list-line"]/dt/a').get_attribute('href')
            nidn = res.find_elements_by_xpath('td/dl[@class="uk-description-list-line"]/dd')[1].text.split(":")[1].replace("</dd>","").strip()
            end2 = timeit.default_timer()
            total2 = end2 - start1
            current2 = tracemalloc.get_traced_memory()
            current2 = current1[0] / 10**6
            chrome_path = r"C:\Users\Asus\Documents\Python Scripts\selenium\chromedriver.exe"
            driver = webdriver.Chrome(chrome_path)
            driver.get(""+str(link_title[0:-8])+"research")
            
            for res in driver.find_elements_by_xpath('//table[@class="uk-table"]/tbody/tr'):
                items = res.find_element_by_xpath('.//dl[@class="uk-description-list-line"]')
                title = items.find_element_by_xpath('.//dt/a').text
                    #link_title = items.xpath('.//dt/a/@href').extract_first().replace("\xa0\xa0 ","")
                skema=items.find_element_by_xpath('.//dd[@class="indexed-by-orange"]').text.replace("\xa0\xa0 ","").strip()
                author2=items.find_elements_by_xpath('.//dd')[1].text.replace("</dd>","").replace("\r\n","").replace("<dd>","").replace("\r\n","").split(",")
                author="";                    
                for author3 in author2 :
                        author = author + ", " + author3.strip() 
                author=author[2:-2]
                date=items.find_elements_by_xpath('.//dd')[2].text.replace("</dd>","").replace("<dd>","").replace("\xa0\xa0\xa0  \r\n                                           ","|").replace("\xa0\xa0\xa0\r\n                                           ","|").strip()
                tema=items.find_elements_by_xpath('.//dd')[3].text.replace("</dd>","").replace("<dd>","").replace("\xa0\xa0 ","").strip()
                sponsor= res.find_element_by_xpath('.//td[@class="uk-text-center"]').text.replace("\xa0\xa0 ","")
                
                a = []
                a.append(title)
                a.append(skema)
                a.append(author)
                a.append(date)
                a.append(tema)
                a.append(sponsor)
                data1=[]
                                                 
                data1.append(tuple(a));print(data1)
                start3 = timeit.default_timer() 
      
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
                