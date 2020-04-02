# -*- coding: utf-8 -*-
import scrapy
import json
import pretty_errors
from bs4 import BeautifulSoup
from goodMenu.items import GoodmenuItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MizunoSpider(CrawlSpider):
	name = 'mizuno'
	start_urls = []

	# rules = [
	#     Rule(
	#         LinkExtractor(allow=('/category/mens/')),
	#         callback = 'parse_list',
	#     )
	# ]

	serial = 0

	def start_requests(self):
		urls = 'https://www.mizunousa.com/category/sports/running/sports+running+apparel.do?c=100262.100269.100356&sortby=bestSellersAscend&pp=100'
		yield scrapy.Request(urls, self.parst_list)

	def parst_list(self, response):
		domain = ['https://www.mizunousa.com']
		soup = BeautifulSoup(response.body, 'lxml')
		for post in soup.select('div.ml-thumb-image-container'):
			yield scrapy.Request(domain[0] + post.select('a')[0]['href'], self.parse_detail)

	def parse_detail(self, response):
		self.serial += 1
		soup = BeautifulSoup(response.body, 'lxml')
		# print(response.url)

		name = soup.select('div.ml-product-name')[0].text.strip().replace('\"','')
		value = soup.select('span.ml-item-price')[0].text.split('.')[0].replace('$','')
		

		crawlitem = GoodmenuItem()
		crawlitem['serial'] = self.serial
		crawlitem['name'] = name
		crawlitem['value'] = value
		return crawlitem
