import pretty_errors
import json
from functools import reduce

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

def backpack(targetSuma, valueList, number): 
    K = [[0 for x in range(targetSum+1)] for x in range(number+1)]  
    for i in range(number+1): 
        for j in range(targetSum+1): 
            if i==0 or j==0: 
                K[i][j] = 0
            elif valueList[i-1] <= j: 
                K[i][j] = max(valueList[i-1] + K[i-1][j-valueList[i-1]],  K[i-1][j]) 
            else: 
                K[i][j] = K[i-1][j] 
  
    return K[number][targetSum] 

number = len(valueList) 
print(backpack(targetSum, valueList, number)) 


 
