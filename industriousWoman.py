import pretty_errors
import json
import numpy as np

# 從 JSON 導入商品清單 & 價格由大到小排序
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
	goodsMenu = json.load(f)
	json = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)
	# print(json)

def backpack(json, target_sum, index = 0):
    if target_sum <= 0:
        return []

    if index >= len(json):
        return None

    item = json[index]
    index += 1
    canTake = min(target_sum // item['value'], item['number'])

    # range(start, stop, step)
    for number in range(canTake, -1, -1):
        path = backpack(json, target_sum - item['value'] * number, index)
        if path != None: 
            if number:
                return path + [{ 'serial': item['serial'], 'value': item['value'], 'number': number, 'name': item['name']}]
            return path

target_sum = int(input('Please enter the Price you want to split : '))
result = backpack(json, target_sum)
print(result)





			



