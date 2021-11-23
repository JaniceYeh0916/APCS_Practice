# 接收資料:
data = int(input())
if data == 0:
    quit()

# 取出因數
number = list(range(data))[1::]
numberList = []
for i in number:
    if (data % i) == 0:
        numberList.append(i)

# 判斷是否為完全數
total = sum(numberList)
if  total == data:
    print('=' + str(data))
    
# 判斷是否有友好數，不是則輸出0
else:
    number = list(range(total))[1::]
    numberList = []
    for t in number:
        if (total % t) == 0:
            numberList.append(t)
    if sum(numberList) == data:
        print(total)
    else:
        print('0')