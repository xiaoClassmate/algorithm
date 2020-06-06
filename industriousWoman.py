import pretty_errors
import json

# 必買物功能
def must_buy(target_sum_list):
    # 導入商品清單(JSON)
    with open("goodsMenu/goodsMenu/json/goodsMenu.json") as f:
        goodsMenu = json.load(f)
    # 輸入必買物，格式：[編號A 數量A 編號B 數量B 編號C 數量C ...]
    must_buy = str(input('請輸入您必須購買的序列號和編號：'))
    print('--------------------------------------------------------------------')
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
        print('--------------------------------------------------------------------')
        print("實際目標總和清單(減過必買物後) " + str(real_target_sum_list))
        print('--------------------------------------------------------------------')
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
    repositories = []
    temp_value = []
    temp_name = []
    for i in range(len(goodsMenu)):
        if goodsMenu[i]["number"] >0:
            for j in range(goodsMenu[i]["number"]):
                temp_value.append(goodsMenu[i]["value"])
                temp_name.append(goodsMenu[i]["name"])

    repositories.append(temp_value)
    print(repositories)
    # 根據拆的筆數，生成多少個 list，例：len(real_target_sum_list) = 3 則生成 [[], [], []]
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
                    print(str(temp_value[j]) +" "+ temp_name[j])
    print('總體最佳解 = {}'.format(min(overall_best_solution) + must_buy_value))
    

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

    # 將剩餘可選的所有組合加到 repositories
    repositories.clear()
    for i in range(len(remainder)):
        repositories.append(remainder[i])

    return [powerSet, powerSet_sum, repositories]
# _______________________________________________________________________________________________________________________

# 使用者輸入要拆的金額
print('--------------------------------------------------------------------')
target_sum = str(input('請輸入您想購買的金額：')) 
print('--------------------------------------------------------------------')

#  建立判斷拆幾筆跟門檻的 list
target_sum_list = [] 

# 將要拆分的門檻依序加入 target_sum_list
# len(target_sum.split(' ')) = 1 表示拆 1 筆，len(target_sum.split(' ')) = 2 表示拆 2 筆，以此類推
for i in range(len(target_sum.split(' '))):
    target_sum_list.append(int(target_sum.split(' ')[i]))
    # 由小到大排序(為了符合大金額放小門檻的原理，小門檻優先拆分)
    target_sum_list = sorted(target_sum_list, reverse=False)

# must_buy(目標門檻陣列) >> 回傳 split_algorithm 需要的參數
must_buy = must_buy(target_sum_list)

# split_algorithm(必買物) >> 回傳 總體最佳解
result = split_algorithm(must_buy)

# _______________________________________________________________________________________________________________________

# DEBUG 專區
# print("real_target_sum_list " + str(real_target_sum_list))
# print("target_sum_list " + str(target_sum_list))
# print(id(變數1), id(變數2))
# print(must_buy_serial)
# print(must_buy_number)
# JSON 索引設定
# goodsMenu[第幾筆][鍵值]，goodsMenu[0]["value"]：表示從 JSON 檔取出第 1 筆的 value
