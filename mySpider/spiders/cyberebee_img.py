from datetime import datetime
from typing import Any

import scrapy
from scrapy import Selector, Request
from scrapy.http import Response

from mySpider.db_dao.db_handle import get_collection
from mySpider.items import ProductionItem


class CyberebeeImgSpider(scrapy.Spider):
    """
    抓取图片
    """
    name = "cyberebee_img"
    allowed_domains = ["www.cyberebee.com"]

    # start_urls = ['https://www.cyberebee.com/Tools-Excipients/Hand-Tool?limit=50']

    def start_requests(self):
        col = get_collection('demo', 'spider1')
        cols = col.find()
        for col in cols:
            # print("col=", col)
            if col['other_image_url1']:
                continue
            yield Request(url=col['source_item_url'], callback=self.parse, cb_kwargs={'col': col})

    def parse(self, response: Response, **kwargs: Any):
        col = kwargs['col']
        product = ProductionItem()
        sel = Selector(response)

        product['source_item_id'] = col['source_item_id']
        product['gmt_modified'] = datetime.now()
        product['collection'] = 'spider1'

        img_list = sel.xpath('//div[contains(@class,"block-content expand-content")]//img')
        # print("img_list size", len(img_list))
        for i, img in enumerate(img_list):
            img_field = 'other_image_url' + str(i + 1)
            if img_field in product.fields:
                img_url = "www.cyberebee.com/" + img.xpath('./@src').extract_first()
                product[img_field] = img_url
        return product
