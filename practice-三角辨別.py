# 接收資料
lengthList = input('')

# 將資料從小到大排序並輸出
lengthList = list(map(int,lengthList.split(' ')))
lengthList.sort()
lengthListStr = list(map(str,lengthList))
print(" ".join(lengthListStr))

# 判斷三角形型態
a,b,c = lengthList
if a + b <= c:
    print('No')
elif a ** 2 + b ** 2 < c ** 2:
    print('Obtuse')
elif a ** 2 + b ** 2 == c ** 2:
    print('Right')
elif a ** 2 + b ** 2 > c ** 2:
    print('Acute')