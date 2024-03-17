# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import logging

import pymongo
import pymysql
from scrapy.exceptions import DropItem

from mySpider.db_dao.db_handle import get_collection
from mySpider.items import ProductionItem, CategoriesItem


class MyspiderPipeline:

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017")
        self.mydb = myclient["demo"]
        # self.collection = self.mydb["cyberebee"]
        self.item_list = []

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        # self.mydb.drop_collection("cyberebee")
        # self.mydb.create_collection("cyberebee")

        if self.item_list:
            item = self.item_list[0]
            collection = self.mydb[item['collection']]
            print("item_list=====", self.item_list)
            collection.insert_many(self.item_list)

    def process_item(self, item, spider):
        print("process_item=====", type(item))

        col = get_collection('demo', item['collection'])
        if isinstance(item, ProductionItem):
            print("process_item2=====", item)
            if not item:
                raise DropItem("Missing data!")
            if item:
                result = col.find_one({'source_item_id': item['source_item_id']})
                if result:
                    # 更新MongoDB数据
                    print("更新MongoDB数据2")
                    col.update_one({'source_item_id': item['source_item_id']},
                                   {'$set': dict(item)})
                else:
                    col.insert_one(dict(item))
        if isinstance(item, CategoriesItem):
            col.insert_one(dict(item))
        logging.info("hello workd")
        return item


class MysqlPipeline:

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('MYSQL_HOST'),
                   database=crawler.settings.get('MYSQL_DATABASE'),
                   user=crawler.settings.get('MYSQL_USER'),
                   password=crawler.settings.get('MYSQL_PASSWORD'),
                   port=crawler.settings.get('MYSQL_PORT'),
                   )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['% s'] * len(data))
        sql = 'insert into % s (% s) values (% s)' % (item.table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class TmpPipeline:

    def process_item(self, item, spider):
        return item
