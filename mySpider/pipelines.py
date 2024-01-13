# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
import logging

from scrapy.exceptions import DropItem


class MyspiderPipeline:

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        mydb = myclient["demo"]
        self.collection = mydb["spider3"]
        self.movie_list = []

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.collection.insert_many(self.movie_list)

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing data!")
        if valid:
            self.movie_list.append(dict(item))
            # self.collection.insert_one(dict(item))
        logging.info("hello workd")
        return item
