from itertools import combinations_with_replacement
import pretty_errors
import json
import sys
sys.setrecursionlimit(1000000)

# 導入商品清單(JSON)
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
    goodsMenu = json.load(f)
    value_list = []
    for i in goodsMenu[:]:
        value_list.append(i['value'])
    value_list.sort(reverse=True)

# 必買物功能
def must_buy(target_sum):
    # 輸入必買物，格式：[編號A 數量A 編號B 數量B 編號C 數量C ...]
    must_buy = str(input('Please enter the serial and number that you must to buy : '))

    # 虛假的輸入值，在布林中被認為是錯誤的
    if(not must_buy):
        real_target_sum = target_sum
        return real_target_sum
    else:
        # 必買物的產品編號
        must_buy_serial = []

        # 必買的數量
        must_buy_number = []

        # 將序號跟數量分別存到各自的 list 中
        must_buy_length = len(must_buy.split(' '))
        for i in range(0, must_buy_length):
            if(i % 2 == 0):
                must_buy_serial.append(int(must_buy.split(' ')[i]))
            else:
                must_buy_number.append(int(must_buy.split(' ')[i]))

        for i in range(0, must_buy_length // 2):
            # JSON 索引設定
            item = goodsMenu[must_buy_serial[i]]

            # 判斷數量是否合乎邏輯
            if item['number'] < must_buy_number[i]:
                return ('產品編號 '+ str(item['serial']) +' ，必買數量超過可接受數量')

            # 實際要拆分的錢 = 拆分的錢 - 必買物價格*數量
            target_sum -= item['value'] * must_buy_number[i]
            real_target_sum = target_sum

            # 印出買了哪些 "必買物"
            print ([{'serial': item['serial'], 'value': item['value'], 'number':must_buy_number[i]}])

            # 紀錄已經拿了幾個，並扣除，避免拿取已經拿過的產品
            item['number'] -= must_buy_number[i]

        # 回傳實際要拆分的錢
        print('實際要拆分 = ' + str(real_target_sum) + ' 元')
        return real_target_sum

        # DEBUG
        # print(must_buy_serial)
        # print(must_buy_number)

def backpack(goodsMenu, real_target_sum, total_price):
    # 商品由大到小排序
    goodsMenu = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)

    # 必買物已經超過門檻，回傳必買物總金額
    if int(real_target_sum) <= 0:
        return '必買物總計 ' + str(target_sum - real_target_sum) + ' 元已經超過門檻 '

    powerSet = []
    subSet_sum_list = []
    answer = 0
    for i in range(1 << len(value_list)):
        subSet = []
        subSet_sum = 0
        for j in range(len(value_list)):
            if i & (1 << j):
                subSet.append(value_list[j])
                subSet_sum += int(value_list[j])
        subSet_sum_list.append(subSet_sum)
        powerSet.append(subSet)
    # print(powerSet)
    # print(subSet_sum_list)
    answer = min(filter(lambda x: x >= real_target_sum, subSet_sum_list))
    print('split = ', real_target_sum)
    print('answer = ', answer)
    path = powerSet[subSet_sum_list.index(answer)]
    print('path = ', path)
    for i in range(len(path)):
        value_list.remove(path[i])
    print('value_list = ', value_list)
    print('-------------------------')
    return answer

# 拆一筆
# target_sum = int(input('Please enter the Price you want to split : '))
# real_target_sum = must_buy(target_sum)
# result = backpack(goodsMenu, real_target_sum)
# print(result)

# 拆兩筆
target_sum = str(input('Please enter the Price you want to split : '))
target_sum_list = []
target_sum_length = len(target_sum.split(' '))
for i in range(target_sum_length):
    target_sum_list.append(int(target_sum.split(' ')[i]))
    target_sum_list = sorted(target_sum_list, reverse=False)
    # print(target_sum_list)

total_price = 0
for i in range(target_sum_length):
    result = backpack(goodsMenu, target_sum_list[i], total_price)
    total_price += result
print('total_price = ', total_price)
