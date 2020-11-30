# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsmenuItem(scrapy.Item):
    # define the fields for your item here like:
    serial = scrapy.Field()
    name = scrapy.Field()
    value = scrapy.Field()
    number = scrapy.Field()