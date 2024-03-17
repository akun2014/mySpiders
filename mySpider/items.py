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
    url = Field()
    description = Field()
    sku = Field()
    features = Field()
    Specification = Field()
    package_includes = Field()
    details_pictures = Field()


class CategoriesItem(Item):
    # collection = 'categories'
    collection = Field()
    url = Field()
    type = Field()


class ProductionItem(Item):
    # 数据集
    collection = Field()
    #############通用字段###################
    target = 'YMX'
    # 商品来源
    source_type = Field()
    source_item_type = Field()
    source_item_id = Field()
    source_item_url = Field()
    source_item_sku = Field()
    source_item_name = Field()
    source_item_url_hash = Field()
    gmt_create = Field()
    gmt_modified = Field()
    status = Field()
    #############通用字段###################
    feed_product_type = Field()
    # 商品sku
    item_sku = Field()
    # IKEN
    brand_name = Field()
    external_product_id = Field()
    external_product_id_type = Field()
    # 标题
    item_name = Field()
    # IKEN
    manufacturer = Field()
    item_type = Field()
    # 价格
    standard_price = Field()
    quantity = Field()
    main_image_url = Field()
    other_image_url1 = Field()
    other_image_url2 = Field()
    other_image_url3 = Field()
    other_image_url4 = Field()
    other_image_url5 = Field()
    other_image_url6 = Field()
    other_image_url7 = Field()
    other_image_url8 = Field()
    update_delete = Field()
    product_description = Field()
    bullet_point1 = Field()
    bullet_point2 = Field()
    bullet_point3 = Field()
    bullet_point4 = Field()
    bullet_point5 = Field()
    package_height = Field()
    package_width = Field()
    package_length = Field()
    package_dimensions_unit_of_measure = Field()
    package_weight = Field()
    package_weight_unit_of_measure = Field()
    #############冗余字段###################
    features = Field()
