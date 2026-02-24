# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GovIfomaGetItem(scrapy.Item):
    # define the fields for your item here like:
    标题 = scrapy.Field()
    企业名称 = scrapy.Field()
    产品商标 = scrapy.Field()
    产品名称 = scrapy.Field()
    产品型号 = scrapy.Field()