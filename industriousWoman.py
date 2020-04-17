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
                item['number'] -= number
                # print({'name': item['name'], 'value': item['value'], 'number': item['number']})
                return path + [{'value': item['value'], 'number': number}]
            # 'serial': item['serial'],
            # 'name': item['name'],
            return path

# 拆一筆
# target_sum = int(input('Please enter the Price you want to split : '))
# result = backpack(json, target_sum)
# print(result)

# 拆兩筆
target_sum = str(input('Please enter the Price you want to split : '))
target_sum_list = []
for i in range(2):
    try:
        target_sum_list.append(int(target_sum.split(' ')[i]))
        target_sum_list = sorted(target_sum_list, reverse=False)
        result = backpack(json, target_sum_list[i])
        print(result)
        # print(target_sum_list)
    except:
        pass

# ------- 測試 -------
# Please enter the Price you want to split : 123 456
# [{'value': 13, 'number': 1}, {'value': 20, 'number': 1}, {'value': 90, 'number': 1}]
# [{'value': 24, 'number': 1}, {'value': 82, 'number': 1}, {'value': 85, 'number': 2}, {'value': 90, 'number': 2}]

# ------- 說明 -------
# json 檔 'value': 90, 'number': 3
# 第一筆 123 已經拿過 1 個 90，因此第二筆 456 剩 2 個 90 可拿

# ------- 結果 -------
# 已完成：'可以剛好拆分'成功，要開始寫反例
# 待完成：其中有無法拆分成功的情況、總體最佳


			



