# Method 1
# 接收資料
data = input()

# 建立英文字母與數字對應表
idList = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,
'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,
'P':23,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,
'X':30,'Y':31,'Z':33}

# 將字母轉成數字
number = idList[data[0]]
newNumber = (number % 10) * 9 + int(number / 10)

# 各數字分別由右到左乘0~8
index = 8
resultList = []
# 利用切片取出數字第一到第八位
for i in data[1:9:]:
    # 將數字乘上規定的參數後存入串列中
    resultList.append(int(i)*index)
    index -= 1

# 算總和
total = newNumber + sum(resultList) + int(data[9])

# 將總和%10判斷餘數是否為0
if total % 10 == 0:
    print('real')
else:
    print('fake')
    


# Method 2
# 接收資料
data = input()

# 建立英文字母與數字對應表
idList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numberList = [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]

# 將字母轉成數字
number = numberList[idList.index(data[0])]
newNumber = (number % 10) * 9 + int(number / 10)

# 各數字分別由右到左乘0~8
index = 8
resultList = []
# 利用切片取出數字第一到第八位
for i in data[1:9:]:
    # 將數字乘上規定的參數後存入串列中
    resultList.append(int(i)*index)
    index -= 1

# 算總和
total = newNumber + sum(resultList) + int(data[9])

# 將總和%10判斷餘數是否為0
if total % 10 == 0:
    print('real')
else:
    print('fake')