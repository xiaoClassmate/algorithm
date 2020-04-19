import pretty_errors
import json

# 導入商品清單(JSON)
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
    goodsMenu = json.load(f)

# 必買物功能
def must_buy(target_sum):

    # 必買物序號
    must_buy = str(input('Please enter the serial and number that you must to buy : '))         
    must_buy_serial = []
    must_buy_number = []
    for i in range(0, len(must_buy_serial)):
        # 將序號跟數量分別存到各自的 list 中
        if(i % 2 == 0):
            must_buy_serial.append(int(must_buy.split(' ')[i]))
        else:
            must_buy_number.append(int(must_buy.split(' ')[i]))

        print(must_buy_number)
        print(must_buy_serial)

        # 根據序號在 JSON 檔中取出與 serial 相對應的 value 值
        item = goodsMenu[must_buy_serial[i]]
        # 實際要拆分的錢 = 拆分的錢 - 必買物價格
        target_sum -= item['value']
        # print(must_buy_number)
        real_target_sum = target_sum
#     # 印出買了哪些 "必買物"
#      print([{'serial': item['serial'], 'value': item['value'], 'number':1}])
# 回傳實際要拆分的錢
# return real_target_sum

# 主要拆分演算法
# def backpack(goodsMenu, real_target_sum, index = 0):

#     # 商品由大到小排序
#     goodsMenu = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)

#     # 必買物已經超過門檻
#     if real_target_sum <= 0:
#         return []

#     if index >= len(goodsMenu):
#         return None

#     # JSON 索引設定
#     item = goodsMenu[index]
#     index += 1
#     canTake = min(real_target_sum // item['value'], item['number'])

#     # 遞迴
#     for number in range(canTake, -1, -1):
#         path = backpack(goodsMenu, real_target_sum - item['value'] * number, index)
#         if path != None: 
#             if number:
#                 item['number'] -= number
#                 # print({'name': item['name'], 'value': item['value'], 'number': item['number']})
#                 return path + [{'serial': item['serial'], 'value': item['value'], 'number': number}]
#             # 'name': item['name'],
#             return path

# 拆一筆
target_sum = int(input('Please enter the Price you want to split : '))
real_target_sum = must_buy(target_sum)
# result = backpack(goodsMenu, real_target_sum)
print(real_target_sum)
# print(result)

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

# ------- 更新 -------
# 4/18 更新：單一必買物完成
# 已完成：單一必買物、拆一筆、拆兩筆
# 待完成：多數必買物、拆兩筆的總體最佳問題

# ------- 拆一筆 + 必買物測試 -------
# Please enter the Price you want to split : 127 (要拆分的錢)
# Please enter the serial you must to buy : 0 1 (必買物的序號)
# [{'value': 14, 'serial': 0, 'number': 1}]
# [{'value': 13, 'serial': 1, 'number': 1}]
# 100 (扣掉必買物後真實要拆分的錢)
# [{'value': 10, 'serial': 4, 'number': 1}, {'value': 90, 'serial': 76, 'number': 1}]

# Please enter the Price you want to split : 123 (要拆分的錢)
# Please enter the serial you must to buy : 1 2 3 (必買物的序號)
# [{'number': 1, 'value': 13, 'serial': 1}]
# [{'number': 1, 'value': 25, 'serial': 2}]
# [{'number': 1, 'value': 30, 'serial': 3}]
# 55 (扣掉必買物後真實要拆分的錢)
# [{'number': 1, 'value': 55, 'serial': 41}]

# ------- 拆兩筆測試 -------
# Please enter the Price you want to split : 123 456
# json 檔 'value': 90, 'number': 3
# 第一筆 123 已經拿過 1 個 90，因此第二筆 456 剩 2 個 90 可拿
# [{'value': 13, 'number': 1}, {'value': 20, 'number': 1}, {'value': 90, 'number': 1}]
# [{'value': 24, 'number': 1}, {'value': 82, 'number': 1}, {'value': 85, 'number': 2}, {'value': 90, 'number': 2}]


			



