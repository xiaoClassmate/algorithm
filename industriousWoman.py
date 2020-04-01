import pretty_errors
import json


# 目標金額輸入
targetSum = int(input('Please enter a split money : '))

# 從 JSON 導入商品清單並由大到小排序價格
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu.json") as f:
	goodsMenu = json.load(f)
	# print(sorted(goodsMenu , key = lambda i: i['value'], reverse=True))
	valueList = []
	for i in goodsMenu:
		valueList.append(i['value'])
	valueList = sorted(valueList, reverse=True)
	print(valueList)

# 列出所有價格組合
# powerSet = []
# for i in range(1 << len(valueList)):
# 	subSet = []
# 	sum = 0
# 	for j in range(len(valueList)):
# 		if i & (1 << j):
# 			subSet.append(valueList[j])
# 			sum = sum + int(valueList[j])
# 	subSet.append(sum)
# 	powerSet.append(subSet)
# print('powerSet = ', powerSet)

# 將價格的所有組合寫入 JSON 檔
# with open("/home/xiao/gitReadWrite/algorithm/powerSet.json", "w") as f:
# 	f.write(str(powerSet))
# 	print("OK")

def backpack(targetSum, valueList, number): 
	res = [[0 for x in range(targetSum+1)] for x in range(number+1)]
	for j in range(targetSum+1):
		res[0][j]=0
	for i in range(1,number+1):
		for j in range(1,targetSum+1):
			res[i][j]=res[i-1][j]
			if j>=valueList[i-1] and res[i][j]<res[i-1][j-valueList[i-1]]+valueList[i-1]:
				res[i][j]=res[i-1][j-valueList[i-1]]+valueList[i-1]
	return res
 
def show(number,targetSum,valueList,res):
	x=[False for i in range(number)]
	j=targetSum
	for i in range(1,number+1):
		if res[i][j]>res[i-1][j]:
			x[i-1]=True
			j-=valueList[i-1]
	print("選擇的物品有 : ")
	sum = 0
	for i in range(number):
		if x[i]:
			print("第", i, "個, value = ", valueList[i])
			sum = sum + valueList[i]
	print("最佳解(Total) : ",sum)

if __name__=='__main__':
	number = len(valueList)
	res=backpack(targetSum,valueList, number)
	show(number,targetSum,valueList,res)

# ---------------------------------------------------------------------
# 測試結果
# xiao@DESKTOP-V1PNS4H:~/gitReadWrite/algorithm$ python3 industriousWoman.py
# Please enter a split money : 321
# [199, 96, 89, 88, 49, 48, 45, 41, 39, 39, 37, 21, 21, 20, 18, 15, 9, 8, 8, 4]
# 選擇的物品有 :
# 第 0 個, value =  199
# 第 1 個, value =  96
# 第 11 個, value =  21
# 第 19 個, value =  4
# 最佳解(Total) :  320
# xiao@DESKTOP-V1PNS4H:~/gitReadWrite/algorithm$ python3 industriousWoman.py
# Please enter a split money : 87
# [199, 96, 89, 88, 49, 48, 45, 41, 39, 39, 37, 21, 21, 20, 18, 15, 9, 8, 8, 4]
# 選擇的物品有 :
# 第 4 個, value =  49
# 第 10 個, value =  37
# 最佳解(Total) :  86
# xiao@DESKTOP-V1PNS4H:~/gitReadWrite/algorithm$ python3 industriousWoman.py
# Please enter a split money : 228
# [199, 96, 89, 88, 49, 48, 45, 41, 39, 39, 37, 21, 21, 20, 18, 15, 9, 8, 8, 4]
# 選擇的物品有 :
# 第 0 個, value =  199
# 第 11 個, value =  21
# 第 17 個, value =  8
# 最佳解(Total) :  228
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# 需要修的 bug
# 不知道為什麼超過輸入超過 390 就會爆炸
# 我就爛
# ---------------------------------------------------------------------
 
