import pretty_errors
import json
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
                return path + [{ 'serial': item['serial'], 'value': item['value'], 'number': number, 'name': item['name']}]
            return path

target_sum = str(input('Please enter the Price you want to split : '))
target_sum_list = []
for i in range(2):
    target_sum_list.append(int(target_sum.split(' ')[i]))
print(target_sum_list)
# result = backpack(json, target_sum)
# print(result)




			



