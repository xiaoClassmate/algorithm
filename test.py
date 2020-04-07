import numpy as np

value_list = [10, 5, 8, 3, 6, 7, 4]
value_length = len(value_list) +1
target_sum = 24

# combination have [10, 3, 7, 4], [8, 3, 7, 6]
dp = np.zeros((value_length+1, target_sum))
dp[2][1] = 3
print("{0}".format(dp))

if(dp[value_length][target_sum] >= target_sum) :
		return dp
	else:
		for i in range(value_length+1):
			for j in range(target_sum+1):
				dp[i][j] = dp[i-1][j]
				if j >= value_list[i-1] and dp[i][j] <= value_list[i-1]:
					dp[i][j] = value_list[i-1]
		return dp
 
def path(value_length, target_sum, value_list, dp):
	x=[False for i in range(value_length)]
	j=target_sum
	for i in range(1,value_length+1):
		if dp[i][j] > dp[i-1][j]:
			x[i-1]=True
			j -= value_list[i-1]
	print("選擇的物品有 : ")
	sum = 0
	for i in range(value_length):
		if x[i]:
			print("第", i, "個, value = ", value_list[i])
			sum += value_list[i]
	print("組合 : ",sum)

if __name__=='__main__':
	target_sum = int(input('Please enter a split money : ')) 
	value_length = len(value_list)
	dp=backpack(target_sum,value_list, value_length)
	path(value_length,target_sum,value_list,dp)

# 列出所有價格組合
# powerSet = []
# for i in range(1 << len(value_list)):
# 	subSet = []
# 	sum = 0
# 	for j in range(len(value_list)):
# 		if i & (1 << j):
# 			subSet.append(value_list[j])
# 			sum = sum + int(value_list[j])
# 	subSet.append(sum)
# 	powerSet.append(subSet)
# print('powerSet = ', powerSet)

# 將價格的所有組合寫入 JSON 檔
# with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json", "w") as f:
# 	f.write(str(powerSet))
# 	print("OK")

	# dp[value_length][0] = True，表示空集合的總和為 0
	# for i in range(value_length+1):
	# 	dp[i][0] = True

	# dp[0][targetSum] = False，表示沒有元素，則無法求總和
	# for j in range(target_sum+1):
	# 	dp[0][j] = False

	# dp = [[0 for x in range(target_sum+1)] for x in range(value_length+1)]
	# dp = np.zeros((value_length+1, target_sum))

	# def backpack(target_sum, value_list, is_used):
	# 	value_length = len(value_list)

	# 	# 沒有物品，就沒有辦法求總和
	# 	if value_length <= 0:
	# 		print("value_list error")

	# 	# 目標金額 0 我要怎麼拆分 ?
	# 	if target_sum <= 0:
	# 		print("target_sum error")

	# 	# 達成目標，return 哪些物品被選
	# 	if sum(is_used) >= target_sum:
	# 		yield is_used
	# 	# 物品全都被拿完了
	# 	elif value_list == []:
	# 		pass
	# 	else:
	# 		# choice
	# 		for i in backpack(target_sum, value_list[:], is_used+[value_list[0]]):
	# 			yield i 
	# 		# not choice
	# 		for i in backpack(target_sum, value_list[1:], is_used):
	# 			yield i 

	# target_sum = int(input('Please enter a split money : ')) 
	# path = ([path for path in backpack(target_sum, value_list, [])])
	# for p in path:
	# 	print(p)

	# print("optimal soultion : ", min(path, key=lambda path:(sum(path)-target_sum)))

	# 設定 value & number 的 list
	# value_list = []
	# number_list = []
	# for i in json:
	# 	value_list.append(i['value'])
	# 	number_list.append(i['number'])
	# value_list = sorted(value_list, reverse=True)


