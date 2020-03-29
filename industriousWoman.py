import pretty_errors
import json

# 目標金額輸入
# targetSum = input('Please enter a split money : ')

# 價格排序
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu.json") as f:
	goodsMenu = json.load(f)
	goodsList = []
	for i in range(len(goodsMenu)):
		goodsList.append(goodsMenu[i])
	print(sorted(goodsList, key = lambda i: i['value'], reverse=True))

sum = 0
backpack = []


 
