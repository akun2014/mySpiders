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
        self.collection = mydb["spider2"]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
            print("data="+data)
            self.collection.insert_one({"name": data.name})
        logging.info("hello workd")
        return item
