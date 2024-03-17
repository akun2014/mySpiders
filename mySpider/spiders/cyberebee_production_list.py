from datetime import datetime

import scrapy
from lxml import etree
from scrapy import Request

from mySpider.db_dao.db_handle import get_collection, is_production_exist
from mySpider.items import ProductionListItem
from mySpider.utils.myUtils import hash_str


class CyberebeeProductionListSpider(scrapy.Spider):
    """
    抓取产品列表
    """
    name = "cyberebee_production_list"
    allowed_domains = ["www.cyberebee.com"]

    # start_urls = ["https://www.cyberebee.com/Tools-Excipients/Hand-Tool"]

    def start_requests(self):
        col = get_collection('demo', 'categories')
        cols = col.find()
        for i, col in enumerate(cols):
            # if i > 2:
            #     continue
            # print("col=", col)
            _url = col['source_url'] + "?limit=2000"
            yield Request(url=_url, callback=self.parse)

    def parse(self, response):
        html = etree.HTML(response.text)
        products = html.xpath('//div[@class="product-layout  has-extra-button"]')
        print("Product len", len(products))

        items = []
        for i, product in enumerate(products):
            # if i > 2:
            #     break
            source_item_url = product.xpath('.//div/div[2]/div[1]/a//@href')[0]
            source_item_id = hash_str(source_item_url)
            if is_production_exist(source_item_id):
                continue
            item = ProductionListItem()
            item['source_type'] = 'cyberebee'
            item['collection'] = 'production_list'
            item['source_item_name'] = product.xpath('.//div/div[2]/div[1]/a//text()')[0]
            item['source_item_url'] = source_item_url
            item['source_item_id'] = source_item_id
            item['source_item_url_hash'] = source_item_id
            item['gmt_create'] = datetime.now()

            items.append(item)
        return items
