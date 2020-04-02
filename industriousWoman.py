import pretty_errors
import json


# 目標金額輸入
# targetSum = int(input('Please enter a split money : '))

# 從 JSON 導入商品清單並由大到小排序價格
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu.json") as f:
	goodsMenu = json.load(f)
	# print(sorted(goodsMenu , key = lambda i: i['value'], reverse=True))
	value_list = []
	for i in goodsMenu:
		value_list.append(i['value'])
	value_list = sorted(value_list, reverse=True)
	# print(value_list)

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
# with open("/home/xiao/gitReadWrite/algorithm/powerSet.json", "w") as f:
# 	f.write(str(powerSet))
# 	print("OK")

def backpack(target_sum, value_list, value_length):
	dp = [[0 for x in range(target_sum+1)] for x in range(value_length+1)]

	# subset[0][targetSum] = False，表示沒有元素，則無法求總和
	for j in range(target_sum+1):
		dp[0][j] = False

	# subset[value_length][0] = True，表示空集合的總和為 0
	for i in range(value_length+1):
		dp[i][0] = True

	if(dp[value_length-1][target_sum] >= target_sum) :
		return dp
	else:
		for i in range(1, value_length+1):
			for j in range(1, target_sum+1):
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

