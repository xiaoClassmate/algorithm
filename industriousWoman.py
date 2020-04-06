import pretty_errors
import json
import numpy as np

# 從 JSON 導入商品清單並由大到小排序價格
value_list = []
number_list = []
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
	goodsMenu = json.load(f)
	# print(sorted(goodsMenu , key = lambda i: i['value'], reverse=True))
	for i in goodsMenu:
		value_list.append(i['value'])
		number_list.append(i['number'])
	value_list = sorted(value_list, reverse=True)
	# ['1', '2', '3'] >> [1, 2, 3] 
	value_list = [int(i) for i in value_list]
	number_list = [int(i) for i in number_list] 
	# print(value_list)
	# print(number_list)

def backpack(target_sum, available, is_used):
	value_length = len(value_list)

	# 沒有物品，就沒有辦法求總和
	if value_length <= 0:
		print("value_list error")

	# 目標金額 0 我要怎麼拆分 ?
	if target_sum <= 0:
		print("target_sum error")

	# 達成目標，return 哪些物品被選
	if sum(is_used) >= target_sum:
		yield is_used
	# 物品全都被拿完了
	elif available == []:
		pass
	else:
		# choice
		for i in backpack(target_sum, available[:], is_used+[available[0]]):
			yield i 
		# not choice
		for i in backpack(target_sum, available[1:], is_used):
			yield i 

target_sum = int(input('Please enter a split money : ')) 
path = ([path for path in backpack(target_sum, value_list, [])])
for p in path:
	print(p)

print("optimal soultion : ", min(path, key=lambda path:(sum(path)-target_sum)))








			



