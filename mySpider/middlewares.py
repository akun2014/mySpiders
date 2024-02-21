# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from logging import getLogger

import selenium
from scrapy.http import HtmlResponse
from selenium import webdriver
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_cookies():
    cookies_str = 'cna=6ZYoHSqaBH4CATpkqlwy6mmU; thw=cn; cookie2=184dfba7061f4e5b280fa7aa297d2dd1; t=1ae9fd11828f2ea032bdd07b316bb7ba; _tb_token_=31ee66b141ba3; _samesite_flag_=true; lgc=qiankun92; cancelledSubSites=empty; dnk=qiankun92; publishItemObj=Ng%3D%3D; tracknick=qiankun92; l=fBai3-ncNiZt9dQKBO5a-urza779wQOf5sPzaNbMiIEGC6YPvqJORLxQVn4TwFKRR8XPMPJJ4M2jj8vTYeP_5PHZndLHRe1VivIHIeTIK7Nk_; mtop_partitioned_detect=1; _uetvid=52fbcd60b14d11ee97ed81bf39e803a2; mt=ci=-1_0; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=3c58e7d7d5b1447aeb38fd1cbfa7ea9f_1705681878767; _m_h5_tk_enc=2001d9e1eaf5e4f0b80b052c0e551220; xlly_s=1; 3PcFlag=1705672465176; sgcookie=E100P%2BjZEMCjnBA5IiYhrdQtRDlw0bWYTVLBwMLjfAXj7%2Fo16dncsXhU6RxCjCIoGLvnRG%2BJZB0dDDWm5YSjvNoY5IYX370sLNgvypDhWOxchsII4Q1NDPjjWzPW8mnbiIhEgeLRotfTOTaJjplrAs1ShQ%3D%3D; unb=925615859; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=WvKSnFLmRjvW&nk2=EvywP7FQwiQV&vt3=F8dD3ChGuTC6lyzyjMw%3D; csg=cd0ec82d; cookie17=WvKSnFLmRjvW; skt=9dcb7fad4a059f73; existShop=MTcwNTY3MjUxMg%3D%3D; uc4=id4=0%40WDWhqC9vaJyA7Q43SY7pGkQZzXs%3D&nk4=0%40EIOda3mS%2B%2BjZGCgPtBU9b5wAuRM%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=299; _nk_=qiankun92; cookie1=W8nVEKDDUzw2qf7%2F0ekUyWERKQnLanMdPCS8qKihgIA%3D; uc1=cookie14=UoYekEW61cb1Zg%3D%3D&cookie21=V32FPkk%2FhoSsNFD%2FenC8JA%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&pas=0; isg=BKSkFC95nb22FugI-ydhSSw4daKWPcinWJ9Ur77FD28yaUUz5kwgN5IKKcHxsQD_; tfstk=eLlWUfOTMgjWz1Blc3TqlpZYb2FIF0OwOwaKS2CPJ7FJOynZcJCeE7yQOmEqauuzwBaKbmwKYkuPrxmZW_lyEW5QZWVpbhRw_T0utWdLUOsirUT15ZKw_CuJezVEkh8oBejcxTswSI5Z7n6OC6eu4NVk7Qd-GrK3X4wUorlbO8ETHo1pPja7Fl3P4J5afCLAdCFVOrZwlE6hK_5Q5DuXi3xuer4J_ETfc928orZwlE6G18U0yh8XlOSC.'
    cookies = {}
    for item in cookies_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        cookies[key] = value
    return cookies


class MyspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class MyspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print("set request cookies")
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class RandomUserAgentDownloaderMiddleware:
    def __init__(self):
        self.user_agents = ['Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
                            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
                            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'
                            ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)


class CookieProcessMiddleware:
    def __init__(self):
        self.need_cookie = ['taobao']

    def process_request(self, request, spider):
        if spider.name in self.need_cookie:
            request.cookies = get_cookies()


class SeleniumMiddleware:
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        用 PhantomJS 抓取页面
        :param request: Request 对象
        :param spider: Spider 对象
        :return: HtmlResponse
        """
        self.logger.debug('Chrome is Starting')
        page = request.meta.get('page', 1)
        try:
            self.browser.get('https://s.taobao.com/search')
            if page > 1:
                searchInput = self.wait.until(
                    EC.presence_of_element_located((By.ID, 'q')))
                submit = self.wait.until(
                    EC.element_to_be_clickable((By.ID, 'button')))
                searchInput.clear()
                searchInput.send_keys(page)
                submit.click()
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(page)))
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
