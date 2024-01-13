# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class MyspiderItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    img_url = scrapy.Field()
    cnt = scrapy.Field()
    direct = scrapy.Field()


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    img_url = scrapy.Field()
    cnt = scrapy.Field()
    direct = scrapy.Field()
    detail_url = scrapy.Field()
    movie_detail = scrapy.Field()
