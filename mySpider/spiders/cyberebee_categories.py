from datetime import datetime

import scrapy

from mySpider.db_dao.db_handle import is_categories_exist
from mySpider.items import CategoriesItem
from mySpider.utils.myUtils import hash_str


class CyberebeeCategoriesSpider(scrapy.Spider):
    """
    抓取类型
    """
    name = "cyberebee_categories"
    allowed_domains = ["www.cyberebee.com"]
    start_urls = ["https://www.cyberebee.com/Automobiles-Motorcycles"]

    def parse(self, response):
        root = scrapy.Selector(response)
        elm = root.xpath("//div[@class = 'accordion-menu accordion-menu-19']")
        a_list = elm.xpath(".//a[starts-with(@href, 'https://www.cyberebee.com')]")
        url_arr = []
        for i, a in enumerate(a_list):
            url = a.xpath("@href").extract_first()
            url_hash = hash_str(url)
            if is_categories_exist(url_hash):
                continue

            item = CategoriesItem()
            item['source_url'] = url
            item['collection'] = 'categories'
            item['source_item_url_hash'] = url_hash
            item['gmt_create'] = datetime.now()
            url_arr.append(item)
        return url_arr
