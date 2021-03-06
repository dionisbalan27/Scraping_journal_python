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
            url = "http://garuda.ristekbrin.go.id/journal/view/1254?page=0&from=2015"
            print(url)
            yield scrapy.Request(get_url(url), callback=self.parse, meta={'position': 0})
            

    def parse(self, response):
        #print(response.url)
        position = response.meta['position']
 
        for res in response.xpath('//div[@class="article-item"]'):
            Title = res.xpath('.//a[@class="title-article"]/xmp/text()').extract_first()
            Link_title = res.xpath('.//a[@class="title-article"]/@href').extract_first()
            print(Title)
            auth2 = ""
            for auth1 in res.xpath('.//a[@class="author-article"]'):
                auth2 = auth1.xpath('.//text()').extract_first() + ";" + auth2
            author = auth2[0:-1]
            print(author)
            indeks = res.xpath('.//xmp[@class="subtitle-article"]/text()').extract_first()
            downloadori =res.xpath('.//p[@class="action-article"]/a[@class="title-citation"]')[0].xpath('./@href').extract_first().strip()
            pdf = res.xpath('.//p[@class="action-article"]/a[@class="title-citation"]')[1].xpath('./@href').extract_first().strip()
            DOI = res.xpath('.//p[@class="action-article"]/a[@class="title-citation"]')[2].xpath('./text()').extract_first().replace("\r\n","").strip()
            data=[]
            a = []
            a.append(Title)
            a.append(author)
            a.append(Link_title)
           
            a.append("Desember 2019" )
            a.append(downloadori)
            a.append(pdf)
            a.append(DOI)
          
            
                           
            data.append(tuple(a));print(data)
    
           