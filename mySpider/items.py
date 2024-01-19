# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


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


class ProductItem(Item):
    collection = 'products'
    image = Field()
    price = Field()
    deal = Field()
    title = Field()
    shop = Field()
    location = Field()