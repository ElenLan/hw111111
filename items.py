# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LabirintparsItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    priceold = scrapy.Field()
    pricenew = scrapy.Field()
    rating = scrapy.Field()
    _id = scrapy.Field()