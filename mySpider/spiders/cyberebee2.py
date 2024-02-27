import scrapy
from lxml import etree
from scrapy import Selector, Request

from mySpider.items import ProductItem



def get_features(elms, title, others):
    if title in {'Details pictures:'}:
        return None
    features = []
    features_find = False
    other_find = False
    for elm in elms:
        tag = elm.tag

        if tag == 'br':
            continue
        # print("tag=", tag)
        if (tag == 'span' or tag == 'strong') and elm.text is not None and elm.text.startswith(
                title) and elm.text.strip() != 'Package Included:':
            # print("====Features txt founded====")
            features_find = True
            continue

        if (tag == 'span' or tag == 'strong') and elm.text is not None and elm.text.strip() in others and features_find:
            # print("====Other txt founded====1")
            other_find = True
            break

        if tag == 'div':
            for e in elm.xpath('.//text()'):
                if e.strip() in others and features_find:
                    # print("====Other txt founded====2")
                    other_find = True
                    break

        if tag == 'img':
            print("====Img txt founded====3")
            break

        if tag == 'strong' and elm.text is not None and elm.text.strip() == 'Package Included:':
            x_elm = elm.xpath('.//text()')
            for e in x_elm:
                if len(e.strip()) == 0 or e.strip() == 'Package Included:' or e.strip() == 'More Details:':
                    continue
                if e.strip() not in features:
                    features.append(e.strip())
            break

        if features_find and (not other_find) and tag != 'br':
            x_elm = elm.xpath('.//text()')
            for e in x_elm:
                if len(e.strip()) == 0:
                    continue
                if e.strip() not in features:
                    features.append(e.strip())
    return features

class Cyberebee2Spider(scrapy.Spider):
    name = "cyberebee2"
    allowed_domains = ["www.cyberebee.com"]
    start_urls = ['https://www.cyberebee.com/Tools-Excipients/Hand-Tool?limit=50']

    def parse(self, response, **kwargs):
        sel = Selector(response)
        products = sel.xpath('//div[@class="product-layout  has-extra-button"]')
        print("Product len", len(products))

        # for product in products:
        for i, product in enumerate(products):
            # print(i)
            # if i != 0:
            #     continue
            item = ProductItem()
            item['title'] = product.xpath('.//div/div[2]/div[1]/a//text()').extract_first()
            detail_url = product.xpath('.//div/div[2]/div[1]/a//@href').extract_first()
            item['url'] = detail_url
            # item['description'] = product.xpath('.//div/div[2]/div[2]//text()').extract_first()
            # item['price'] = product.xpath('.//div/div[2]/div[3]/span//text()').extract_first()
            req = Request(url=detail_url, callback=self.parse_detail, cb_kwargs={
                'product': item
            })
            yield req

    def parse_detail(self, response, **kwargs):
        product = kwargs['product']
        sel = Selector(response)
        item_detail = sel.xpath('//div[contains(@class,"block-content expand-content")]')

        product['sku'] = sel.xpath(
            ' // *[ @ id = "product"] / div[3] / div[2] / ul / li[2]/span//text()').extract_first()
        product['price'] = sel.xpath('//*[@id="product"]/div[3]/div[1]/div[1]/div//text()').extract_first().replace('$', '')
        img_list = sel.xpath('//div[contains(@class,"block-content expand-content")]//img')
        print("img_list size", len(img_list))
        imgs = []
        for img in img_list:
            imgs.append("www.cyberebee.com/" + img.xpath('./@src').extract_first())
        product['image'] = imgs

        others_el = {'Package included:', 'Details pictures:', 'Package Included:',
                     'Specification:', 'Description:', 'Features:', 'More Details:'}
        html = etree.HTML(response.text)
        e_tmp = html.xpath('//div[contains(@class,"block-content expand-content")]//*')
        product['features'] = get_features(e_tmp, 'Features:', others_el)

        desc = get_features(e_tmp, 'Description:', others_el)
        pkg_inc1 = get_features(e_tmp, 'Package Included:', others_el)
        pkg_inc2 = get_features(e_tmp, 'Package included:', others_el)
        spec = get_features(e_tmp, 'Specification:', others_el)

        pkg = []
        if len(pkg_inc1) > 0:
            for d in pkg_inc1:
                if d not in pkg:
                    pkg.append(d)
        if len(pkg_inc2) > 0:
            for d in pkg_inc2:
                if d not in pkg:
                    pkg.append(d)
        specification = []
        if len(spec) > 0:
            for d in spec:
                if d not in specification:
                    specification.append(d)

        description = "<b>Description</b><br>"
        if len(desc) > 0:
            for d in desc:
                description += d + "<br>"

        if len(specification) > 0:
            description += "<br><b>Specification</b><br>"
            for d in specification:
                description += d + "<br>"

        if len(pkg) > 0:
            description += "<br><b>Package Included:</b><br>"
            for d in pkg:
                description += d + "<br>"

        product['description'] = description

        yield product
