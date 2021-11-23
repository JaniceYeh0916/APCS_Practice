# 接收資料
number = int(input(''))
scoreList = input('')

# 將資料從小到大排序並輸出
scoreList = list(map(int,scoreList.split(' ')))
scoreList.sort()
scoreListStr = list(map(str,scoreList))
print(" ".join(scoreListStr))

# 分析資料，將資料分割為及格與不及格兩個部分
passList = []
fallList = []
for score in scoreList:
    if score < 60:
        fallList.append(score)
    else:
        passList.append(score)
        
# 從不及格部分中找出最大者並輸出，若資料數為零，則輸出best case
if len(fallList) == 0:
    print('best case')
else:
    print(fallList[-1])
# 從及格部分中找出最小者并輸出，若資料數為零，則輸出worse case
if len(passList) == 0:
    print('worst case')
else:
    print(passList[0])
