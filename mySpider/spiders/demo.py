import scrapy
from scrapy import Selector


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/subject/1292052/"]

    def parse(self, response):
        sel = Selector(response)
        article_list = sel.xpath('//span[@property="v:summary"]/text()').extract_first()
        yield {
            'article_list': article_list.strip()
        }
