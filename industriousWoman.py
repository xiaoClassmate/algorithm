import pretty_errors
import json

# 導入商品清單(JSON檔)
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
    goodsMenu = json.load(f)

# 必買物功能
def must_buy(target_sum):
    must_buy = str(input('Please enter the serial you must to buy : '))         
    must_buy_list = []
    must_buy_path = []
    must_buy_length = len(must_buy.split(' '))
    for i in range(0, must_buy_length):
        must_buy_list.append(int(must_buy.split(' ')[i]))
        item = goodsMenu[must_buy_list[i]]
        # print(item['value'])
        target_sum -= item['value']
        real_target_sum = target_sum
        print([{'serial': item['serial'], 'value': item['value'], 'number':1}])
    return real_target_sum


# 主要拆分演算法
def backpack(goodsMenu, real_target_sum, index = 0):

    # 商品由大到小排序
    goodsMenu = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)

    # 必買物已經超過門檻
    if real_target_sum <= 0:
        return []

    if index >= len(goodsMenu):
        return None

    # JSON 索引設定
    item = goodsMenu[index]
    index += 1
    canTake = min(real_target_sum // item['value'], item['number'])

    # 遞迴
    for number in range(canTake, -1, -1):
        path = backpack(goodsMenu, real_target_sum - item['value'] * number, index)
        if path != None: 
            if number:
                item['number'] -= number
                # print({'name': item['name'], 'value': item['value'], 'number': item['number']})
                return path + [{'serial': item['serial'], 'value': item['value'], 'number': number}]
            # 'name': item['name'],
            return path

# 拆一筆
target_sum = int(input('Please enter the Price you want to split : '))
real_target_sum = must_buy(target_sum)
result = backpack(goodsMenu, real_target_sum)
print(real_target_sum)
print(result)

# 拆兩筆
# target_sum = str(input('Please enter the Price you want to split : '))
# target_sum_list = []
# target_sum_length = len(target_sum.split(' '))
# for i in range(target_sum_length):
#     try:
#         target_sum_list.append(int(target_sum.split(' ')[i]))
#         target_sum_list = sorted(target_sum_list, reverse=False)
#         result = backpack(json, target_sum_list[i])
#         print(result)
#         # print(target_sum_list)
#     except:
#         pass

# ------- 測試 -------
# Please enter the Price you want to split : 123 456
# [{'value': 13, 'number': 1}, {'value': 20, 'number': 1}, {'value': 90, 'number': 1}]
# [{'value': 24, 'number': 1}, {'value': 82, 'number': 1}, {'value': 85, 'number': 2}, {'value': 90, 'number': 2}]

# ------- 說明 -------
# json 檔 'value': 90, 'number': 3
# 第一筆 123 已經拿過 1 個 90，因此第二筆 456 剩 2 個 90 可拿

# ------- 結果 -------
# 4/18 更新：單一必買物完成
# ---------------------
# 已完成：'可以剛好拆分'成功
# 待完成：多筆必買物、其中有無法拆分成功的情況、總體最佳


			



