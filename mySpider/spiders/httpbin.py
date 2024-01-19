import scrapy


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org"]

    def parse(self, response):
        self.logger.debug(response.request.headers)
