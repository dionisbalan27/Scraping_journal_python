# -*- coding: utf-8 -*-
import scrapy
import tracemalloc
import mysql.connector
from urllib.parse import urlencode
from urllib.parse import urlparse
import json
import timeit
from datetime import datetime
from time import sleep

API_KEY = '66749ed54fe5f5fd56a83888e0ac6f65'

def get_url(url):
    payload = {'api_key': API_KEY, 'url': url, 'country_code': 'us'}
    proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
    return proxy_url



data1=[];data=[]
class ExampleSpider(scrapy.Spider):
    name = 'scholar'
    allowed_domains = ['api.scraperapi.com']
    global start1

    start1 = timeit.default_timer()  

    def start_requests(self):
        
        queries = ['airbnb']
        for query in queries:
            url = "https://sinta.ristekbrin.go.id/departments/detail?page=0&afil=6&id=22201&view=authors&sort=year2"
            print(url)
            yield scrapy.Request(get_url(url), callback=self.parse, meta={'position': 0})
            
  
    def parse(self, response):
            end1 = timeit.default_timer()
            total1 = end1 - start1 
            current1 = tracemalloc.get_traced_memory()
            current1 = current1[0] / 10**6
            start2 = timeit.default_timer()  
          
            #print(response.url)
       
            for res in response.xpath('//table[@class="uk-table"]/tbody/tr'):
                image = res.xpath('.//img[@class="author-photo-small uk-align-left"]/@src').extract_first()
                title = res.xpath('.//td/dl[@class="uk-description-list-line"]/dt/a/text()').extract_first()
                link_title = res.xpath('.//td/dl[@class="uk-description-list-line"]/dt/a/@href').extract_first()
                nidn = res.xpath('.//td/dl[@class="uk-description-list-line"]/dd').extract()[1].split(":")[1].replace("</dd>","").strip()
                end2 = timeit.default_timer()
                total2 = end2 - start1
                current2 = tracemalloc.get_traced_memory()
                current2 = current1[0] / 10**6
                a = []
                a.append(title)
                a.append(link_title)
                a.append(image)
                a.append(nidn)
                data.append(tuple(a))
                global urls
                urls="https://sinta.ristekbrin.go.id"+str(link_title[0:-8])+"research"
                print(urls)
                yield scrapy.Request(get_url(urls), callback=self.parse2, meta={'position': 0})
                             
                data.append(tuple(a));
    def parse2(self, response):
          
                for res in response.xpath('//table[@class="uk-table"]/tbody/tr'):
                    items = res.xpath('.//dl[@class="uk-description-list-line"]')
                    title = items.xpath('.//dt/a/text()').extract_first()
                    #link_title = items.xpath('.//dt/a/@href').extract_first().replace("\xa0\xa0 ","")
                    skema=items.xpath('.//dd[@class="indexed-by-orange"]/text()').extract_first().replace("\xa0\xa0 ","").strip()
                    author2=items.xpath('.//dd').extract()[1].replace("</dd>","").replace("\r\n","").replace("<dd>","").replace("\r\n","").split(",")
                    author="";                    
                    for author3 in author2 :
                        author = author + ", " + author3.strip() 
                    author=author[2:-2]
                    date=items.xpath('.//dd').extract()[2].replace("</dd>","").replace("<dd>","").replace("\xa0\xa0\xa0  \r\n                                           ","|").replace("\xa0\xa0\xa0\r\n                                           ","|").strip()
                    tema=items.xpath('.//dd').extract()[3].replace("</dd>","").replace("<dd>","").replace("\xa0\xa0 ","").strip()
                    sponsor= res.xpath('.//td[@class="uk-text-center"]/text()').extract_first().replace("\xa0\xa0 ","")
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