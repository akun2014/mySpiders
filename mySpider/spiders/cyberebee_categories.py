import scrapy

from mySpider.items import CategoriesItem


class CyberebeeCategoriesSpider(scrapy.Spider):
    name = "cyberebee_categories"
    allowed_domains = ["www.cyberebee.com"]
    start_urls = ["https://www.cyberebee.com/Automobiles-Motorcycles"]

    def parse(self, response):
        root = scrapy.Selector(response)
        elm = root.xpath("//div[@class = 'accordion-menu accordion-menu-19']")
        a_list = elm.xpath(".//a[starts-with(@href, 'https://www.cyberebee.com')]")
        url_arr = []
        for a in a_list:
            item = CategoriesItem()
            url = a.xpath("@href").extract_first()
            item['url'] = url
            url_arr.append(item)
        return url_arr
