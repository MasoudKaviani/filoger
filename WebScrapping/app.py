import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
import json
import time
import hashlib
import os

class DataCollector(CrawlSpider):
    name = 'https://www.isna.ir'
    allowed_domains = ['www.isna.ir']
    start_urls = ['https://www.isna.ir']
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if 'isna.ir/news' in response.url:
            title = response.css('h1.first-title::text').get()
            description = response.css('#item .content-full-news .summary::text').get()
            with open('isna.txt', 'a', encoding='utf-8') as f:
                f.write(str(response.url.encode('utf-8')) + ',' + str(title.encode('utf-8')) + ',' + str(description.encode('utf-8')) + '\n')

# scrapy runspider app.py
# MasoudKaviani.ir