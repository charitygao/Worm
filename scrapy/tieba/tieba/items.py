# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    favour = scrapy.Field()
    user = scrapy.Field()
    user_info = scrapy.Field()
    content = scrapy.Field()
    pass
