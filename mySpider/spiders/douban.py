import scrapy
from mySpider.items import MyspiderItem as ItcastItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/latest?subcat=小说"]

    def parse(self, response):


        for item in response.xpath('//*[@id="content"]/div/div[1]/ul/li'):
            data = ItcastItem()
            print(item)
            data['name'] = item.xpath('/html/body/div[3]/div[1]/div/div[1]/ul/li[1]/div[2]/p[1]').extract()[0]
            yield data
