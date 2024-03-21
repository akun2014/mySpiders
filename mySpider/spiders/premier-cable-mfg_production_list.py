from datetime import datetime

import scrapy
from scrapy import Request

from mySpider.db_dao.db_handle import get_collection
from mySpider.items import ProductionListItem
from mySpider.utils.myUtils import hash_str


class CyberebeeProductionListSpider(scrapy.Spider):
    """
    抓取产品列表
    """
    name = "premier-cable-mfg_production_list"
    allowed_domains = ["www.premier-cable-mfg.com"]

    # start_urls = ["https://www.premier-cable-mfg.com/product/57/"]

    def start_requests(self):
        col = get_collection('demo', 'premier-cable-mfg')
        cols = col.find()
        for i, col in enumerate(cols):
            # if i > 1:
            #     continue
            print("col=", col)
            _url = col['source_url']
            yield Request(url=_url, callback=self.parse)

    def parse(self, response):
        base_url = "https://www.premier-cable-mfg.com"
        root = scrapy.Selector(response)
        products = root.xpath('//ul[@class="product-list clearfix"]/li')
        print("Product len", len(products))

        items = []
        for i, product in enumerate(products):
            # if i > 2:
            #     break
            source_item_url = base_url + product.xpath('.//a/@href').extract_first()
            source_item_id = hash_str(source_item_url)
            item = ProductionListItem()
            item['collection'] = 'production_list'
            item['source_type'] = 'premier-cable-mfg'
            item['source_item_name'] = product.xpath('.//figcaption[@class="proName"]/text()').extract_first()
            item['source_item_url'] = source_item_url
            item['source_item_id'] = source_item_id
            item['source_item_url_hash'] = source_item_id
            item['gmt_create'] = datetime.now()

            items.append(item)
        return items
