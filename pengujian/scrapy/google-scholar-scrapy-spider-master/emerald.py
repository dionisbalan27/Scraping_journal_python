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

data=[]
class ExampleSpider(scrapy.Spider):
    name = 'scholar'
    allowed_domains = ['api.scraperapi.com']
    global start 
    start=timeit.default_timer()
    tracemalloc.start()
    def start_requests(self):
        global start1

        start1 = timeit.default_timer()  
        tracemalloc.start()
        queries = ['airbnb']
        for query in queries:
            url = "https://www.emerald.com/insight/search?q=diponegoro+university&advanced=true&fromYear=2015&toYear=2020&ipp=50&p=0"
            print(url)
            yield scrapy.Request(get_url(url), callback=self.parse, meta={'position': 0})
            
  
    def parse(self, response):
            #print(response.url)
            position = response.meta['position']
            end1 = timeit.default_timer()
            total1 = end1 - start1 
            current1 = tracemalloc.get_traced_memory()
            current1 = current1[0] / 10**6
            start2 = timeit.default_timer()  
            for res in response.xpath('//div[@class="intent_search_result container card-shadow is-animated Search-item__wrapper"]'):
                title = res.xpath('.//div/h2[@class="h3 mt-0 mb-2"]/a/span[@class="intent_title"]/text()').extract_first()
                link_title = res.xpath('.//div/h2[@class="h3 mt-0 mb-2"]/a/@href').extract_first()
                author=""
                for resauth in res.xpath('.//p[@class="my-3 medium font-weight-light"]/a'):
                   author=author+resauth.xpath("text()").extract_first()+", " 
                position += 1
                a = []
                a.append(title)
                a.append(author)
                end2 = timeit.default_timer()
                total2 = end2 - start1
                current2 = tracemalloc.get_traced_memory()
                current2 = current1[0] / 10**6
                data1=[]
                data1.append(tuple(a))
         
                db = mysql.connector.connect(
        host="localhost",user="root",passwd="",db="scrape" )
                cursor = db.cursor()
                sql = "INSERT INTO pbp_book(Nama, Jurusan, Nidn, Judul, Isbn, Author, Publisher, pld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
                    
                for values in data1:
                        cursor.execute(sql, values)
                        db.commit()
                end3 = timeit.default_timer()
                total3 = end3 - start1
                    
                current3 = tracemalloc.get_traced_memory()
                current3 = current3[0] / 10**6
                db.close()
        
               
