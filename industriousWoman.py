import itertools
import pretty_errors
import json
import numpy as np

# 導入商品清單(JSON)
with open("goodsMenu/goodsMenu/json/goodsMenu.json") as f:
    goodsMenu = json.load(f)
    # value_list = []
    # for i in goodsMenu[:]:
    #     value_list.append(i['value'])
    # value_list.sort(reverse=True)

# 必買物功能
def must_buy(target_sum_list):
    # 輸入必買物，格式：[編號A 數量A 編號B 數量B 編號C 數量C ...]
    must_buy = str(input('Please enter the serial and number that you must to buy : '))
    print('--------------------------------------------------------------------')

    # 全域變數(global)會解決一切
    global real_target_sum_list

    # 寫 real_target_sum_list = target_sum_list 只會讓兩個相等 ... 要讓左邊附值到右邊請加 list
    real_target_sum_list = list(target_sum_list)

    # 沒有必買物，直接回傳目標門檻等於真正的目標門檻
    if(not must_buy):
        # for i in range(len(target_sum_list)):
        #     real_target_sum_list.append(target_sum_list[i])
        return real_target_sum_list
    # 否則就有必買物，目標門檻扣除必買物等於真正要拆分的目標門檻
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
            real_target_sum_list[0] -= item['value'] * must_buy_number[i]

            # 印出買了哪些 "必買物"
            print ([{'serial': item['serial'], 'value': item['value'], 'number':must_buy_number[i]}])
            print ('--------------------------------------------------------------------')

            # 紀錄已經拿了幾個，並扣除，避免拿取已經拿過的產品
            item['number'] -= must_buy_number[i]

        # 回傳實際要拆分的錢
        print("real_target_sum_length " + str(real_target_sum_list))
        print ('--------------------------------------------------------------------')
        return real_target_sum_list

def split_algorithm(goodsMenu, real_target_sum_list, target_sum_list):
    # 商品根據金額由大到小排序
    goodsMenu = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)

    # JSON 索引設定
    # goodsMenu[第幾筆][鍵值]，goodsMenu[0]["value"]：表示從 JSON 檔取出第 1 筆的 value

    # 必買物已經超過門檻，回傳必買物總金額
    if int(real_target_sum_list[0]) <= 0:
        return '門檻一必買物總計 ' + str(target_sum_list[0] - real_target_sum_list[0]) + ' 元已經超過門檻'

    # 計算現在正在跑到第幾筆門檻
    count = 0

    # 倉庫的初值設定(用來跑遞迴每一層的所有組合)
    repositories = []
    temp = []
    for i in range(len(goodsMenu)):
        temp.append(goodsMenu[i]["value"])
    repositories.append(temp)

    # 拆幾筆就需要遞迴幾次
    answer_1 = []
    answer_1_path = []
    answer_2 = []
    answer_2_path = []
    answer_sum = []
    for i in range(len(real_target_sum_list)):
        resursion_record = recursion(repositories, count)
        powerSet = resursion_record[0]
        powerSet_sum = resursion_record[1]
        repositories = resursion_record[2]
        if i == 0:
            answer_1.extend(powerSet_sum)
            answer_1_path.extend(powerSet)
        else:
            answer_2.extend(powerSet_sum)
            answer_2_path.extend(powerSet)
        count += 1
    try:
        answer_sum = [a + b for a, b in zip(answer_1, answer_2)]
        print('總體最佳為 ' + str(min(answer_sum)))
        index = answer_sum.index(min(answer_sum))
        print('第一筆 ' + str(answer_1[index]) + str(answer_1_path[index]))
        print('第二筆 ' + str(answer_2[index]) + str(answer_2_path[index]))
    except:
        print('總體最佳為 ' + str(min(answer_1)))
        index = answer_1.index(min(answer_1))
        print('第一筆 ' + str(answer_1[index]) + str(answer_1_path[index]))

    
def recursion(repositories, count):
    # repositories 扣除 powerSet 後剩餘可選
    remainder_list = []
    # 滿足大於等於門檻的所有組合
    powerSet = []
    # 其中每一筆組合的總和
    powerSet_sum = []
    # repositories 有幾個 list 就跑幾次
    for repo in range(len(repositories)):
        subSet_filter = []
        # 計算組合數
        for i in range(1 << len(repositories[repo])):
            subSet = []
            subSet_sum = 0
            # 取 or 不取
            for j in range(len(repositories[repo])):
                if i & (1 << j):
                    subSet.append((repositories[repo])[j])
                    subSet_sum += int((repositories[repo])[j])
                # 將符合門檻的取出來並停止
                if subSet_sum >= real_target_sum_list[count]:
                    if subSet not in subSet_filter:
                        subSet_filter.append(subSet)
                    break
        if count == 0:
            powerSet.extend(subSet_filter)
        else:
            subSet_filter_minus = []
            for i in range(len(subSet_filter)):
                subSet_filter_minus.append(sum(subSet_filter[i]))
            index = subSet_filter_minus.index(min(subSet_filter_minus))
            powerSet.append(subSet_filter[index])

    # 依據 powerSet 求出 powerSet_sum
    for i in range(len(powerSet)):
        powerSet_sum.append(sum(powerSet[i]))

    for i in range(len(powerSet)):
        try:
            remainder_list.append(list(repositories[i]))
        except:
            remainder_list.append(list(repositories[0]))
        for j in range(len(powerSet[i])):
            try:
                remainder_list[i].remove((powerSet[i])[j])
            except:
                pass

    # 將剩餘可選的所有組合加到 repo
    repositories.clear()
    for i in range(len(remainder_list)):
        repositories.append(remainder_list[i])

    return powerSet, powerSet_sum, repositories    
# _______________________________________________________________________________________________________________________

# 使用者輸入要拆的金額
print('--------------------------------------------------------------------')
target_sum = str(input('Please enter the price you want to split : ')) 
print('--------------------------------------------------------------------')

#  建立判斷拆幾筆跟門檻的 list
target_sum_list = [] 

# 將要拆分的門檻依序加入 target_sum_list
# len(target_sum.split(' ')) 是計算 target_sum 的長度 = 1 表示拆 1 筆，len(target_sum.split(' ')) = 2 表示拆 2 筆，以此類推
for i in range(len(target_sum.split(' '))):
    target_sum_list.append(int(target_sum.split(' ')[i]))
    # 由小到大排序(為了符合大金額放小門檻的原理，小門檻優先拆分)
    target_sum_list = sorted(target_sum_list, reverse=False)

# must_buy(目標門檻陣列) >> 回傳 真正的目標門檻金額
real_target_sum_list = must_buy(target_sum_list)

# split_algorithm(JSON, 真正的目標門檻金額) >> 回傳 總體最佳解
result = split_algorithm(goodsMenu, real_target_sum_list, target_sum_list)

# _______________________________________________________________________________________________________________________

# DEBUG 專區
# print("real_target_sum_length " + str(real_target_sum_list))
# print("target_sum_length " + str(target_sum_list))
# print(id(變數1), id(變數2))
# powerSet_comb = []
# powerSet_comb = list(itertools.combinations(powerSet_sum, 2))
# print(must_buy_serial)
# print(must_buy_number)

# 格式化輸出
# for i in range(len(powerSet)):
#     print('{} - {} ({}) = {}'.format(temp, powerSet[i], powerSet_sum[i], remainder_list[i]))
# print('{}'.format(repositories))