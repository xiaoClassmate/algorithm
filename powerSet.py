priceList = [20, 33, 50, 18]
powerSet = []
for i in range(1 << len(priceList)):
	subSet = []
	sum = 0
	for j in range(len(priceList)):
		if i & (1 << j):
			subSet.append(priceList[j])
			sum = sum + int(priceList[j])
	subSet.append(sum)
	powerSet.append(subSet)
print('powerSet = ', powerSet)