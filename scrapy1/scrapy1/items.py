# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    up_image = scrapy.Field()
    introduces = scrapy.Field()
    intros = scrapy.Field()
    low_image = scrapy.Field()
    cili = scrapy.Field()
    pass
