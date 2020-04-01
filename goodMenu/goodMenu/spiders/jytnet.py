# -*- coding: utf-8 -*-
import scrapy
import pretty_errors
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup
from goodMenu.items import GoodmenuItem

class JytnetSpider(CrawlSpider):
    name = 'jytnet'
    allowed_domains = ['www.jytnet.com.tw']
    start_urls = []

    def start_requests(self):
    	urls = 'http://www.jytnet.com.tw//ap/catalog.aspx?filter=4362F42D-4751-4ED1-A58F-6B68B224B12E&count=200&code='
    	for i in range(1, 19):
    		next_urls = urls + str(i)
    		yield  scrapy.Request(next_urls, self.parse_list)

    def parse_list(self, response):
    	soup = BeautifulSoup(response.body, 'lxml')
    	# print('-----------------------------------------------')
    	# print(response.url)
    	# print('-----------------------------------------------')

    	global name
    	global price

    	for i in range(20):
    		try:
	    		name = soup.select('td p')[i].text
	    		if name == '目前無任何資料':
	    			name = ''
	    		price = soup.select('td li span')[i].text.replace('特價', '').replace('元','')
	    	except:
	    		pass
 		
    	item = GoodmenuItem()
    	item['name'] = name
    	# item['price'] = price
    	return item