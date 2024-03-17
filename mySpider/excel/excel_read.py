import json

with open("../bizdata/metadata.json", 'r') as meta_data:
    biz_data = json.load(meta_data)
    head_map = {}
    for data in biz_data:
        head_map[data['column_name']] = data['idx']


def get_head_idx(head_name):
    if head_name not in head_map:
        # print("Key " + head_name + " does not exist.")
        return None
    return head_map[head_name]


print(get_head_idx("feed_product_type"))
