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
        
        queries = ['airbnb']
        for query in queries:
            url = "https://www.emerald.com/insight/search?q=diponegoro+university&advanced=true&fromYear=2015&toYear=2020&ipp=50&p=0"
            print(url)
            yield scrapy.Request(get_url(url), callback=self.parse, meta={'position': 0})
            
  
    def parse(self, response):
            #print(response.url)
            position = response.meta['position']
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage connection is {current / 10**6}MB; Peak was {peak / 10**6}MB")
            tracemalloc.start()
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
              
                                             
                data.append(tuple(a));
                current2, peak2 = tracemalloc.get_traced_memory()
                print(f"Current memory usage scraping is {current2 / 10**6}MB; Peak was {peak2 / 10**6}MB")
                end_scrap = timeit.default_timer();total_scrap = end_scrap - start;
                print("waktu eksekusi scrraping dan koleksi data :",total_scrap,"s")
                start_db = timeit.default_timer(); 
                tracemalloc.start()
            
                item = {'title': title,'author': author,'link title': link_title}
                print(item)
                yield item
            
               
