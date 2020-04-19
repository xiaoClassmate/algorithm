import pretty_errors
import json

# 導入商品清單(JSON)
with open("/home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json") as f:
    goodsMenu = json.load(f)

# 必買物功能
def must_buy(target_sum):
    # 輸入必買物
    must_buy = str(input('Please enter the serial and number that you must to buy : '))         
    # 必買物的產品編號
    must_buy_serial = []
    # 必買的數量
    must_buy_number = []
    must_buy_length = len(must_buy.split(' '))
    print(must_buy_length)

    for i in range(0, must_buy_length):
        # 將序號跟數量分別存到各自的 list 中
        if(i % 2 == 0):
            must_buy_serial.append(int(must_buy.split(' ')[i]))
        else:
            must_buy_number.append(int(must_buy.split(' ')[i]))

    # DEBUG 用
    # print(must_buy_serial)
    # print(must_buy_number)

    for i in range(0, must_buy_length // 2):
        # 根據序號在 JSON 檔中取出與 serial 相對應的 value 值
        item = goodsMenu[must_buy_serial[i]]

        # 判斷數量是否合乎邏輯
        if item['number'] < must_buy_number[i]:
            print('產品編號 '+ str(item['serial']) +' ，必買數量超過可接受數量')

        # 實際要拆分的錢 = 拆分的錢 - 必買物價格*數量
        target_sum -= item['value'] * must_buy_number[i]
        real_target_sum = target_sum

        # 印出買了哪些 "必買物"
        print([{'serial': item['serial'], 'value': item['value'], 'number':must_buy_number[i]}])

    # 回傳實際要拆分的錢
    return real_target_sum

# 主要拆分演算法
def backpack(goodsMenu, real_target_sum, target_sum, index = 0):
    # 商品由大到小排序
    goodsMenu = sorted(goodsMenu , key = lambda i: i['value'], reverse=True)

    # 必買物已經超過門檻
    if real_target_sum <= 0:
        # 回傳必買物總金額
        return target_sum - real_target_sum

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
result = backpack(goodsMenu, real_target_sum, target_sum)
print(real_target_sum)
print(result)

# 拆兩筆
target_sum = str(input('Please enter the Price you want to split : '))
target_sum_list = []
target_sum_length = len(target_sum.split(' '))
for i in range(target_sum_length):
    try:
        target_sum_list.append(int(target_sum.split(' ')[i]))
        target_sum_list = sorted(target_sum_list, reverse=False)
        result = backpack(json, target_sum_list[i])
        print(result)
        # print(target_sum_list)
    except:
        pass

# ------- 更新 -------
# 4/18 更新：單一、多筆必買物完成
# 已完成：單一必買物、拆一筆、拆兩筆
# 待完成：拆兩筆的總體最佳問題

