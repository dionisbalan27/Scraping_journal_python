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

start = timeit.default_timer()

        
if offset <= 999999 :
    if offset <= 999999 :
    # url = "https://www.sciencedirect.com/search?affiliations=diponegoro%20university"
        chrome_path = r"D:\TA\mysql\pengujian\selenium\chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)
        driver.get("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=universitas+diponegoro")
       
        for res in driver.find_elements_by_xpath('//div[@id="gs_res_ccl_mid"]/div[@id="gs_r gs_or gs_scl"]'):
                title = res.find_element_by_xpath('.//h3[@class="gs_rt"]/a').text
                link_title = res.find_element_by_xpath('.//h3[@class="gs_rt"]/a/@href').get_attribute('href')
                author = res.find_element_by_xpath('.//div[@id="gs_a"]/a').text
                citation = res.find_element_by_xpath('.//div[@id="gs_fl"]/a[3]').text
            
                a = []
                a.append(title)
                a.append(link_title)
                a.append(author)
                a.append(citation)
                data=[]
                data.append(tuple(a))
                print(data)