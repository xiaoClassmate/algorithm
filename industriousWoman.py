import pretty_errors
import json
# import sys
# sys.setrecursionlimit(100000)
import numpy as np

# json import goodsMenu.json & sort value with decreasing order
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
                return path + [{'value': item['value'], 'number': number}]
            # 'serial': item['serial'],
            # 'name': item['name'],
            return path

# 分一筆
# target_sum = int(input('Please enter the Price you want to split : '))
# result = backpack(json, target_sum)
# print(result)

# 分兩筆
target_sum = str(input('Please enter the Price you want to split : '))
target_sum_list = []
for i in range(2):
    try:
        target_sum_list.append(int(target_sum.split(' ')[i]))
        result = backpack(json, target_sum_list[i])
        print(result)
    except:
        pass

# 已完成：兩筆輸入後跑演算法
# 待完成：紀錄哪些產品跑過要扣掉
# ------- 測試 -------
# Please enter the Price you want to split : 300 666
# [{'value': 30, 'number': 1}, {'value': 90, 'number': 3}]
# [{'value': 24, 'number': 1}, {'value': 32, 'number': 1}, {'value': 85, 'number': 4}, {'value': 90, 'number': 3}]





			



