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
            url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=universitas+diponegoro&btnG="
            print(url)
            yield scrapy.Request(get_url(url), callback=self.parse, meta={'position': 0})
            
  
    def parse(self, response):
         
            #print(response.url)
       
            for res in response.xpath('//div[@id="gs_res_ccl_mid"]/div[@id="gs_r gs_or gs_scl"]'):
                title = res.xpath('.//h3[@class="gs_rt"]/a/text()').extract_first()
                link_title = res.xpath('.//h3[@class="gs_rt"]/a/@href').extract_first()
                author = res.xpath('.//div[@id="gs_a"]/a/text()').extract_first()
                citation = res.xpath('.//div[@id="gs_fl"]/a[3]/text()').extract_first()
            
                a = []
                a.append(title)
                a.append(link_title)
                a.append(author)
                a.append(citation)
                data.append(tuple(a))
                print(data)
   