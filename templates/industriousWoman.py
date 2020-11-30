import pretty_errors
import json
import time
from urllib import request
import re

# 必買物功能
def must_buy(target_sum_list):
    # 導入商品清單(JSON)
    with open("goodsMenu/goodsMenu.json") as f:
         goodsMenu = json.load(f)


    # 輸入必買物，格式：[編號A 數量A 編號B 數量B 編號C 數量C ...]
    #must_buy = str(input('請輸入您必須購買的序列號和編號：'))
    must_buy = 0
    print('--------------------------------------------------------------------')

    # 測試執行時間
    global start
    start = time.time()

    # 全域變數(global)會解決一切
    global real_target_sum_list

    # 寫 real_target_sum_list = target_sum_list 只會讓兩個相等 ... 要讓左邊附值到右邊請加 list
    real_target_sum_list = list(target_sum_list)

    # 沒有必買物
    if(not must_buy):
        # 必買物總價 = 0
        must_buy_value = 0
        # 直接回傳
        return [target_sum_list, real_target_sum_list, goodsMenu, must_buy_value]
    # 否則就有必買物，目標門檻扣除必買物等於真正要拆分的目標門檻
    else:
        # 必買物的產品編號
        must_buy_serial = []
        # 必買的數量
        must_buy_number = []
        # 將序號跟數量分別存到各自的 list 中，因為格式是 [編號，數量，編號，數量] mod 2 取餘數
        for i in range(len(must_buy.split(' '))):
            if(i % 2 == 0):
                must_buy_serial.append(int(must_buy.split(' ')[i]))
            else:
                must_buy_number.append(int(must_buy.split(' ')[i]))
        must_buy_value = 0
        for i in range(len(must_buy.split(' ')) // 2):
            # JSON 索引設定
            item = goodsMenu[must_buy_serial[i]]
            # 判斷數量是否合乎邏輯
            if item['number'] < must_buy_number[i]:
                return ('產品編號 '+ str(item['serial']) +' ，必買數量超過可接受數量')
            # 必買物總價
            must_buy_value += item['value'] * must_buy_number[i]
            # 實際要拆分的錢 = 拆分的錢 - 必買物價格*數量 (備註，這個寫法爛到不行)
            for v in range(must_buy_number[i]):
                if real_target_sum_list[0] > 0:
                    real_target_sum_list[0] -= item['value']
                else:
                    real_target_sum_list[1] -= item['value']
            # 買了哪些 "必買物"
            print ([{'serial': item['serial'], 'value': item['value'], 'number':must_buy_number[i], 'name':item['name']}])
            # 紀錄已經拿了幾個，並扣除，避免拿取已經拿過的產品
            item['number'] -= must_buy_number[i]

        return [target_sum_list, real_target_sum_list, goodsMenu, must_buy_value]

def split_algorithm(must_buy):
    # 必買物傳值設定
    target_sum_list = must_buy[0]
    real_target_sum_list = must_buy[1]
    goodsMenu = must_buy[2]
    must_buy_value = must_buy[3]

    # 商品根據金額由大到小排序
    goodsMenu = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)

    # 必買物已經超過所有門檻，回傳必買物總金額
    for x in range(len(real_target_sum_list)):
        if real_target_sum_list[x] <= 0:
            print('門檻' + str(x) + '必買物總計 ' + str(target_sum_list[x] - real_target_sum_list[x]) + ' 元已經超過門檻')

    # 計算現在正在跑到第幾筆門檻
    count = 0

    # 倉庫的初值設定(用來跑遞迴每一層的所有組合)
    global temp_value, repositories, temp_name
    repositories = []
    temp_value = []
    temp_name = []
    for i in range(len(goodsMenu)):
        if goodsMenu[i]["number"] >0:
            for j in range(goodsMenu[i]["number"]):
                temp_value.append(goodsMenu[i]["value"])
                temp_name.append(goodsMenu[i]["name"])
    repositories.append(temp_value)

    # 根據拆的筆數，生成多少個 list，例：len(real_target_sum_list) = 3 則生成 [[], [], []]
    global answer_list, answer_path, overall_best_solution
    calculate = [[] for i in range(len(real_target_sum_list))]
    answer_list = [[] for i in range(len(real_target_sum_list))]
    answer_path = [[] for i in range(len(real_target_sum_list))]
    overall_best_solution = []

    for i in range(len(real_target_sum_list)):
        resursion_record = recursion(repositories, count)
        powerSet = resursion_record[0]
        powerSet_sum = resursion_record[1]
        repositories = resursion_record[2]
        calculate[i].extend(powerSet_sum)
        answer_list[i].extend(powerSet_sum)
        answer_path[i].extend(powerSet)
        count += 1

    for i in range(len(real_target_sum_list)-1):
        calculate[i+1] = [e1 + e2 for e1, e2 in zip(calculate[i], calculate[i+1])]
    overall_best_solution = calculate[-1]
    index = overall_best_solution.index(min(overall_best_solution))

    for i in range(len(real_target_sum_list)):
        print('第' + str(i) + '筆 = {}, path = {}'.format(answer_list[i][index], answer_path[i][index]))
        repositories = (answer_path[i][index])
        # 顯示商品名稱
        for j in range(len(temp_value)):
            for k in range(len(repositories)):
                if temp_value[j] == repositories[k]:                
                    print(str(temp_value[j]) + " " + temp_name[j])

    print('總體最佳解 = {}'.format(min(overall_best_solution) + must_buy_value))
    print('--------------------------------------------------------------------')

    # 結束執行時間測量並顯示
    global end
    end = time.time()
    # print("執行時間：%f 秒" % (end - start))
    

def recursion(repositories, count):
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
            subSet_sum_list = 0 #紀錄subSet_sum的前一個數值
            # 取 or 不取
            for j in range(len(repositories[repo])):
                if i & (1 << j):
                    subSet.append((repositories[repo])[j])
                    subSet_sum_list = subSet_sum
                    subSet_sum += int((repositories[repo])[j])
                # 將符合門檻的取出來並 break 跳出
                if (subSet_sum >= real_target_sum_list[count]) and (subSet_sum_list <= real_target_sum_list[count]):
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

    # repositories 扣除 powerSet 後剩餘可選
    remainder = []
    for i in range(len(powerSet)):
        try:
            remainder.append(list(repositories[i]))
        except:
            remainder.append(list(repositories[0]))
        for j in range(len(powerSet[i])):
            try:
                remainder[i].remove((powerSet[i])[j])
            except:
                pass

    # 判斷剩餘價格是否大於等於下一個門檻
    remainder_len = len(remainder)
    while(remainder_len >= 0):
        try:
            if(sum(remainder[remainder_len]) < real_target_sum_list[count+1]):
                powerSet.remove(powerSet[remainder_len])
                try:
                    remainder.remove(remainder[remainder_len])
                except:
                    pass
        except:
            pass
        remainder_len -= 1;

    # 將剩餘可選的所有組合加到 repositories
    repositories.clear()
    for i in range(len(remainder)):
        repositories.append(remainder[i])

    return [powerSet, powerSet_sum, repositories]
# _______________________________________________________________________________________________________________________

def run_algo():
    # 使用者輸入要拆的金額
    url = 'https://test-b2aac.firebaseio.com/goods.json'
    json_data = request.urlopen(url).read().decode("utf-8")
    goodlist = [json_data]
    f = open('static/list/threshold.json', 'w+')
    f.writelines(goodlist)
    f.close()

    with open("static/list/threshold.json") as f:
             buyMenu = json.load(f)

    print('--------------------------------------------------------------------')
    target_sum_list=[]
    #target_sum = str(input('請輸入您想購買的金額：')) 
    for b in range(len(buyMenu)):
        print (str(buyMenu[b]["buy"]))
        target_sum_list.append((buyMenu[b]["buy"]))
        target_sum_list = list(target_sum_list)
        target_sum_list.sort()
    #print(target_sum_list)    
    print('--------------------------------------------------------------------')

    # must_buy(目標門檻陣列) >> 回傳 split_algorithm 需要的參數
    global must_buy 
    must_buy = must_buy(target_sum_list)

    # split_algorithm(必買物) >> 回傳 總體最佳解
    try:
        result = split_algorithm(must_buy)
    except:
        print('你的商品總額不足以拆分門檻')

    # 回傳資料到 server.py
    ST = ''
    index = overall_best_solution.index(min(overall_best_solution))
    for i in range(len(real_target_sum_list)):
        ST += str('第' + str(i) + '筆 = {}, path = {}'.format(answer_list[i][index], answer_path[i][index]))
        repositories = (answer_path[i][index])
        for j in range(len(temp_value)):
            for k in range(len(repositories)):
                if temp_value[j] == repositories[k]:                
                    print(str(temp_value[j]) + " " + temp_name[j])
    ST += '總體最佳解 = {} \n'.format(min(overall_best_solution))
    return str(ST) 