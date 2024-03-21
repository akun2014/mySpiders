from datetime import datetime

import scrapy

from mySpider.db_dao.db_handle import is_categories_exist
from mySpider.items import CategoriesItem
from mySpider.utils.myUtils import hash_str


class PremierCableMfgCategoriesSpider(scrapy.Spider):
    """
    抓取类型
    """
    name = "premier-cable-mfg_categories"
    allowed_domains = ["www.premier-cable-mfg.com"]
    start_urls = ["https://www.premier-cable-mfg.com/products1.html"]

    def parse(self, response):
        base_url = "https://www.premier-cable-mfg.com"
        root = scrapy.Selector(response)
        a_list = root.xpath(".//a[starts-with(@href, '/product/')]")
        url_arr = []
        for i, a in enumerate(a_list):
            url = base_url + a.xpath("@href").extract_first()

            item = CategoriesItem()
            item['source_url'] = url
            item['collection'] = 'categories'
            item['source_type'] = 'premier-cable-mfg'
            item['source_item_url_hash'] = hash_str(url)
            item['gmt_create'] = datetime.now()
            url_arr.append(item)
        return url_arr
