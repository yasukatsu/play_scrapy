# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LevtechItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    fee = scrapy.Field()
    job_content = scrapy.Field()
    # nearest_station = scrapy.Field()
    # prefecture = scrapy.Field()
    # job_title = scrapy.Field()
    # development_enviroment = scrapy.Field()
    # required_skill = scrapy.Field()
