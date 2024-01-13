import scrapy


class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["stack.com"]
    start_urls = ["https://stack.com"]

    def parse(self, response):
        pass
