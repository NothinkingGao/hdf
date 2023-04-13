# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 这里定义爬取的数据结构

import scrapy
from scrapy.item import Item, Field


class HdfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FamousDoctorItem(Item):
     name = Field()
     title = Field()
     image = Field()
     hospital = Field()
     status  = Field()

class CommonDoctorItem(Item):
    image = Field()
    name  = Field()
    grade = Field()
    hospital = Field()
    goodat   = Field()


