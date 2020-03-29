# def mergeSort(priceList):
# 	if len(priceList) > 1:
# 		middle = len(priceList) // 2
# 		left = priceList[:middle]
# 		right = priceList[middle:]

# 		mergeSort(left)
# 		mergeSort(right)

# 		L = 0 # iterator for traversing the left
# 		R = 0 # iterator for traversing the right
# 		K = 0 # Iterator for the main list

# 		# sort with decreasing order
# 		while L < len(left) and R < len(right):
# 			if left[L] > right[R]:
# 				priceList[K] = left[L]
# 				L += 1
# 			else:
# 				priceList[K] = right[R]
# 				R += 1
# 			K += 1

# 		# for all the remaining values
# 		while L < len(left):
# 			priceList[K] = left[L]
# 			L += 1
# 			K += 1

# 		while R < len(right):
# 			priceList[K] = right[R]
# 			R += 1
# 			K += 1

priceList = [20, 33, 50, 18]
priceList.sort()
priceList.reverse()
# mergeSort(priceList)






