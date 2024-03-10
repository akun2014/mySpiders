import base64
import random
import string
from datetime import datetime

from bson import ObjectId
from marshmallow import Schema, fields, post_load
from pymongo import MongoClient


class ObjectIdField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return str(value)


class People:
    def __init__(self, name, age, _id=None):
        self.name = name
        self.age = age
        self._id = None
        self.hash_id = hash(name)
        self._id = ObjectId(_id)
        self.gmt_create = datetime.now()
        self.gmt_modified = None


class PeopleSchema(Schema):
    name = fields.Str()
    hash_id = fields.Str()
    age = fields.Integer()
    _id = ObjectIdField()

    @post_load
    def make_user(self, data, **kwargs):
        return People(**data)


def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test"]
    return db


def get_collection(db_name, collection):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    col = db[collection]
    return col


def is_exist(source_item_id):
    coll = get_collection('demo', 'cyberebee')
    result = coll.find_one({"source_item_id": source_item_id})
    # print("result=", result)
    if result:
        return True
    else:
        return False

def main():
    # 获取或创建名为 "my_collection" 的集合
    col = get_db().get_collection("my_collection")

    elm = {"name": "Alice", "age": random.randint(20, 25)}

    # 插入一条文档
    # result = col.insert_one(elm)
    print("Inserting document: ", elm)

    # class 'dict'
    # 查询单一
    # doc1 = col.find_one({"name": "Alice"})
    ## dict is not empty
    # print(doc1["_id"])
    # print(doc1)
    # print(is_exist("Alice"))

    # 存在
    if is_exist(elm["name"]) and elm['age'] > 20:
        user = PeopleSchema().load(elm)
        print("deserialized_user type=", type(user))
        print("deserialized_user=", PeopleSchema().dump(user))

        user.gmt_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print("user=", PeopleSchema(exclude=["_id"]).dump(user))

        result = col.update_many({"name": "Alice"}, {"$set": PeopleSchema(exclude=["_id"]).dump(user)})
        print("Inserted document: ", PeopleSchema().dump(result))
    # 不存在
    else:
        col.insert_one(elm)
        print("Inserted document: ", elm)

    # 查询所有文档
    documents = list(col.find())
    for doc in documents:
        print(doc)

    # class 'pymongo.cursor.Cursor'
    # 分页查询
    # doc2 = col.find({"name": "Alice"}).sort("age", -1).limit(1)
    # for doc in doc2:
    #     print(doc.get("name"))

    # # 更新第一条文档
    # updated_count = col.update_one({"name": "Alice"}, {"$set": {"age": 26}})
    # print(f"Updated {updated_count.modified_count} documents")
    #
    # # 删除第一条文档
    # deleted_count = col.delete_one({"name": "Alice"})
    # print(f"Deleted {deleted_count.deleted_count} documents")

    # 关闭客户端连接
    # client.close()


if __name__ == "__main__":
    str = 'https://www.cyberebee.com/Tools-Excipients/Hand-Tool/0-10cm-ABS-Black-Universal-Pitch-Gauge-For-Esky-Belt-CP-V2-KING-3-Replace-EK1-0348'
    hh = base64.b64encode(bytes(str, 'utf-8'))
    print(hh.decode("utf-8"))
    # print(string(hh,'UTF-8'))
    result = is_exist(hh)
    is_exist(7988236538042432086)
    print(result)

    import hashlib

    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    print(md5.hexdigest())
