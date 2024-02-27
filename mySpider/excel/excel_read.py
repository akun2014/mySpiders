import json

with open("../bizdata/metadata.json", 'r') as meta_data:
    biz_data = json.load(meta_data)
    head_map = {}
    for data in biz_data:
        head_map[data['column_name']] = data['idx']


def get_head_idx(head_name):
    return head_map[head_name]


print(get_head_idx("feed_product_type"))
