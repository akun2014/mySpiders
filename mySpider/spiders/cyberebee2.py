from datetime import datetime
from typing import Any

import scrapy
from lxml import etree
from scrapy import Selector, Request
from scrapy.http import Response

from mySpider.db_dao.db_handle import get_collection
from mySpider.items import ProductionItem


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

    # start_urls = ['https://www.cyberebee.com/Tools-Excipients/Hand-Tool?limit=50']

    def start_requests(self):
        col = get_collection('demo', 'cyberebee')
        cols = col.find({'status': 'NEW'})
        for col in cols:
            print("col=", col)
            yield Request(url=col['source_item_url'], callback=self.parse, cb_kwargs={'col': col})

    def parse(self, response: Response, **kwargs: Any):
        col = kwargs['col']
        product = ProductionItem()
        sel = Selector(response)

        product['source_item_id'] = col['source_item_id']
        product['status'] = 'DONE'
        product['gmt_modified'] = datetime.now()

        product['item_name'] = sel.xpath('//*[@id="product"]/div[1]//text()').extract_first()
        product['item_sku'] = sel.xpath(
            ' // *[ @ id = "product"] / div[3] / div[2] / ul / li[2]/span//text()').extract_first()
        product['standard_price'] = sel.xpath(
            '//*[@id="product"]/div[3]/div[1]/div[1]/div//text()').extract_first().replace('$', '')
        img_list = sel.xpath('//div[contains(@class,"block-content expand-content")]//img')
        print("img_list size", len(img_list))
        for i, img in enumerate(img_list):
            if i >= 8:
                continue
            img_url = "www.cyberebee.com/" + img.xpath('./@src').extract_first()
            img_field = 'other_image_url' + str(i + 1)
            product[img_field] = img_url

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

        product['product_description'] = description

        return product
