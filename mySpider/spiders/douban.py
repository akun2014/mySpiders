import scrapy
from mySpider.items import MyspiderItem as ItcastItem
from mySpider.items import MovieItem
from scrapy import Selector, Request, Spider


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    def parse(self, response, **kwargs):
        sel = Selector(response)
        article_list = sel.css('#content > div > div.article > ol > li')
        for item in article_list:
            data = MovieItem()
            img_url = item.css('div > div.pic > a > img::attr(src)').extract_first()
            title = item.css('div > div.info > div.hd > a > span:nth-child(1)::text').extract_first()
            cnt = item.css('div > div.info > div.bd > div > span:nth-child(4)::text').extract_first()
            direct = item.css('div > div.info > div.bd > p:nth-child(1)::text').extract_first()
            detail_url = item.css('div > div.info > div.hd > a::attr(href)').extract_first()
            data['img_url'] = img_url
            data['title'] = title
            data['cnt'] = cnt
            data['direct'] = direct
            data['detail_url'] = detail_url
            req = Request(url=detail_url, callback=self.parse_detail, cb_kwargs={
                'movie_item': data
            })
            yield req

    def parse_detail(self, response, **kwargs):
        movie_item = kwargs['movie_item']
        sel = Selector(response)
        # link-report-intra > span:nth-child(1)
        # link-report-intra > span.short > span
        # // *[ @ id = "link-report-intra"] / span[1] / span
        # / html / body / div[3] / div[1] / div[2] / div[1] / div[3] / div / span[1] / span
        movie_detail = sel.xpath(' // *[ @ id = "link-report-intra"] / span[1] / span/text()').extract_first()
        movie_item['movie_detail'] = movie_detail
        yield movie_item
