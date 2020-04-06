import pretty_errors
import json
import numpy as np

# 從 JSON 導入商品清單並由大到小排序價格
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
	goodsMenu = json.load(f)
	# print(sorted(goodsMenu , key = lambda i: i['value'], reverse=True))
	value_list = []
	for i in goodsMenu:
		value_list.append(i['value'])
	value_list = sorted(value_list, reverse=True)
	# print(value_list)

def backpack(target_sum, current_sum, value_list, value_length):
	dp = [[0 for x in range(target_sum+1)] for x in range(value_length+1)]
	# dp = np.zeros((value_length+1, target_sum))

	# 沒有物品，就沒有辦法求總和
	if value_length <= 0:
		print("value_list error")

	# 目標金額 0 我要怎麼拆分 ?
	if target_sum <= 0:
		print("target_sum error")

	for i in range(value_length+1):
		for j in range(target_sum+1):
			dp[i][j] = max(dp[i-1][j], dp[i-1][j]+int(value_list[i]))
			current_sum = dp[i][j]
			if current_sum >= target_sum:
				break



