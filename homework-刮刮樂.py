luckyNumber = input().split()
lotteryNumber = input().split()
lotteryBouns = input().split()
# 值 in 串列   判斷值是否存在串列中
# 串列.index(值)   查詢值所在的索引值
money = 0
print(luckyNumber)
# 1.將第一個幸運號碼拿來比對是否中獎
if luckyNumber[0] in lotteryNumber:
    # 2.若第一個獎號中獎，則取出中獎獎金並保存
    # 取出中獎號碼所在位置
    currentIndex = lotteryNumber.index(luckyNumber[0])
    # 至相應位置取出獎金
    money = money + int(lotteryBouns[currentIndex])
    print('目前金額',money)

# 3.將第二個幸運號碼拿來比對是否中獎
if luckyNumber[1] in lotteryNumber:
    # 4.若第二個獎號中獎，則取出中獎獎金並保存
    currentIndex = lotteryNumber.index(luckyNumber[1])
    money = money + int(lotteryBouns[currentIndex])
    print('目前金額',money)

# 5.將第三個幸運號碼拿來比對是否中獎
if luckyNumber[2] in lotteryNumber:
    # 6.若第三個獎號中獎，則將目前的獎金扣除對應的金額
    # 如果低於0元，則保持0元即可
    currentIndex = lotteryNumber.index(luckyNumber[2])
    money = money - int(lotteryBouns[currentIndex])
else:
    # 7.若第三個獎號沒中獎，則將目前的獎金加倍
    money = money * 2
# 8.輸出結果
if money < 0:
    money = 0
print('目前金額',money)