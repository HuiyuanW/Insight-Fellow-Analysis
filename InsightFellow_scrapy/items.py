# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InsightfellowItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Title = scrapy.Field()
    Company = scrapy.Field()
    Project = scrapy.Field()
    Background = scrapy.Field()

