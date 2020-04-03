# -*- coding: utf-8 -*-
import scrapy


class MizunoSpider(scrapy.Spider):
    name = 'mizuno'
    allowed_domains = ['www.mizunousa.com']
    start_urls = ['http://www.mizunousa.com/']

    def parse(self, response):
        pass
