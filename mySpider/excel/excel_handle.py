from openpyxl import load_workbook

from mySpider.items import ProductionItem
from mySpider.utils.cyberebeeUtils import handle_feature, handle_bullet_points
from mySpider.utils.myUtils import hash_str

file_path = "C:/Users/cainiao/Documents/爬虫/天猫商店/cyberebee01.xlsx"
wb = load_workbook(filename=file_path, read_only=False, keep_vba=True)

ws = wb.active
header = {}
item_list = []

for r_num, row in enumerate(ws.iter_rows(values_only=False)):
    item = ProductionItem()
    for index, cell in enumerate(row):
        if r_num == 0:
            header[index] = cell.value
        else:
            item[header[index]] = cell.value
    if r_num > 0:
        item_list.append(item)

for item in item_list:
    item['manufacturer'] = 'IKEN'
    item['update_delete'] = 'update'
    item['quantity'] = 0
    item['standard_price'] = item['standard_price'].replace('$', '')
    item['source_item_id'] = hash_str(item['source_item_url'])
    item['source_item_url_hash'] = hash_str(item['source_item_url'])
    item['item_name'] = item['source_item_name']
    item['bullet_point1'] = handle_feature(item['features'])

    bullet_points = handle_feature(item['features'])
    if 'Features:' in bullet_points:
        # print("bullet_points=", bullet_points['Features:'])
        points = handle_bullet_points(bullet_points['Features:'])
        print("bullet_points=", handle_bullet_points(bullet_points['Features:']))
        for index, point in enumerate(points):
            num = index + 1
            item['bullet_point' + str(num)] = point

print(item_list[0])
