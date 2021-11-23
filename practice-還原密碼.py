# 接收資料
data = list(map(int,input().split()))
number = input()

# 找出要加入的數字
total = 0
letter2 = 0
for i in range(len(number)):
    total += int(number[i])

if total < 10:
    letter = data[1] - total
else:
    totalStr =  str(total)
    total2 = 0
    count = 0
    for i in range(len(totalStr)):
        total2 += int(totalStr[i])
        count = data[1] - total2

    if count > 0:
        letter = count
    elif count == 0 :
        letter = count
        total3 = 0
        count = 0
        letter2 = count = (data[1] - int(totalStr[0]) - 1) + 10 * (int(totalStr[0]) + 1) - total
    else:
        total3 = 0
        count = 0
        letter = count = (data[1] - int(totalStr[0]) - 1) + 10 * (int(totalStr[0]) + 1) - total

# 加入數字
element = []
resultList = []
for i in range(len(number)):
    element.append(number[i])
for i in range(len(number)+1):
    element.insert(i,str(letter))
    resultList.append(" ".join(element))
    element.pop(i)

if letter2 != 0:
    for i in range(len(number)+1):
        element.insert(i,str(letter2))
        resultList.append(" ".join(element))
        element.pop(i)

# 扣掉最大及最小的數字
resultListInt = []
for i in range(len(resultList)):
    resultListInt.append(resultList[i].replace(' ',''))
ansList = list(set(resultListInt))
ansList.sort()
ansList.pop()
ansList.remove(ansList[0])

# 輸出答案
for i in range(len(ansList)):
    print(str(ansList[i]))


