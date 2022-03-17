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
            url = "https://sinta.ristekbrin.go.id/departments/detail?page=0&afil=6&id=22201&view=authors&sort=year2"
            print(url)
            yield scrapy.Request(get_url(url), callback=self.parse, meta={'position': 0})
            
  
    def parse(self, response):
         
            #print(response.url)
       
            for res in response.xpath('//table[@class="uk-table"]/tbody/tr'):
                image = res.xpath('.//img[@class="author-photo-small uk-align-left"]/@src').extract_first()
                title = res.xpath('.//td/dl[@class="uk-description-list-line"]/dt/a/text()').extract_first()
                link_title = res.xpath('.//td/dl[@class="uk-description-list-line"]/dt/a/@href').extract_first()
                nidn = res.xpath('.//td/dl[@class="uk-description-list-line"]/dd').extract()[1].split(":")[1].replace("</dd>","").strip()
           
                a = []
                a.append(title)
                a.append(link_title)
                a.append(image)
                a.append(nidn)
                data.append(tuple(a))
                global urls
                urls="https://sinta.ristekbrin.go.id"+str(link_title[0:-8])+"ipr"
                print(urls)
                yield scrapy.Request(get_url(urls), callback=self.parse2, meta={'position': 0})
                             
                data.append(tuple(a));
    def parse2(self, response):
          
                for res in response.xpath('//table[@class="uk-table"]/tbody/tr'):
                    items = res.xpath('.//dl[@class="uk-description-list-line bookmeta"]')
                    title = items.xpath('.//dt/h4/text()').extract_first()
                    ID=items.xpath('.//dd[1]/span/text()').extract_first()
                    kategori=items.xpath('.//dd[2]/span/text()').extract_first()
                    holder=items.xpath('.//dd[3]/span/text()').extract_first().replace("\n","").strip()
                    inv1=items.xpath('.//dd[4]')
                    inventor=""
                    for inv2 in inv1.xpath('.//li'):
                        inventor=inventor + "," + inv2.xpath('.//a/text()').extract_first()
                    inventor=inventor[1:]
                    
                    data1=[]
                    a = []
                    a.append(title)
                    a.append(ID)
                    a.append(kategori)
                    a.append(holder)
                    a.append(inventor)
                   
                                                 
                    data1.append(tuple(a));print(data1)