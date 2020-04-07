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

# ------------------------- 測試結果 ---------------------------------

name = 商品名稱
serial = 商品編號
value = 商品價格
number = 商品數量

# Please enter the Price you want to split : 102
# [{'name': 'TRAINING SOCKS MID 3-PACK', 'serial': 99, 'number': 1, 'value': 12},
# {'name': "Men's Breath Thermo® Half Zip", 'serial': 76, 'number': 1, 'value': 90}]

# 90*1 + 12*1 = 102

# Please enter the Price you want to split : 79
# [{'number': 1, 'serial': 49, 'name': 'WARMALITE PIP', 'value': 24},
# {'number': 1, 'serial': 41, 'name': "MEN'S AERO 4.5 SHORT 2.0", 'value': 55}]

# 55*1 + 21*1 = 79

# Please enter the Price you want to split : 327
# [{'number': 1, 'value': 12, 'serial': 99, 'name': 'TRAINING SOCKS MID 3-PACK'},
# {'number': 1, 'value': 45, 'serial': 53, 'name': "Men's Alpha 9 Running Shorts"},
# {'number': 3, 'value': 90, 'serial': 76, 'name': "Men's Breath Thermo® Half Zip"}]

# 90*3 + 45*1 + 12*1 = 327

# Please enter the Price you want to split : 666
# [{'value': 24, 'number': 1, 'serial': 49, 'name': 'WARMALITE PIP'},
# {'value': 32, 'number': 1, 'serial': 7, 'name': "Women's Patriotic Tank"},
# {'value': 85, 'number': 4, 'serial': 52, 'name': "Men's Breath Thermo® Base Layer Long Sleeve"},
# {'value': 90, 'number': 3, 'serial': 76, 'name': "Men's Breath Thermo® Half Zip"}]

# 90*3 + 85*4 + 32*1 + 24*1 = 666


			



