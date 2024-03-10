from datetime import datetime

import scrapy
from lxml import etree
from scrapy import Request

from mySpider.db_dao.db_handle import is_exist, get_collection
from mySpider.items import ProductionItem
from mySpider.utils.myUtils import hash_str


class ProductListSpider(scrapy.Spider):
    name = "product_list"
    allowed_domains = ["www.cyberebee.com"]

    # start_urls = ["https://www.cyberebee.com/Tools-Excipients/Hand-Tool"]

    def start_requests(self):
        col = get_collection('demo', 'categories')
        cols = col.find()
        for col in cols:
            print("col=", col)
            yield Request(url=col['url'], callback=self.parse)

    def parse(self, response):
        html = etree.HTML(response.text)
        products = html.xpath('//div[@class="product-layout  has-extra-button"]')
        print("Product len", len(products))

        items = []
        for i, product in enumerate(products):
            source_item_url = product.xpath('.//div/div[2]/div[1]/a//@href')[0]
            source_item_id = hash_str(source_item_url)
            if is_exist(source_item_id):
                continue
            item = ProductionItem()
            item['source_type'] = 'cyberebee'
            item['source_item_name'] = product.xpath('.//div/div[2]/div[1]/a//text()')[0]
            item['source_item_url'] = source_item_url
            item['source_item_id'] = hash_str(source_item_url)
            item['source_item_url_hash'] = hash_str(source_item_url)
            item['status'] = 'NEW'
            item['gmt_create'] = datetime.now()

            items.append(item)
        return items
