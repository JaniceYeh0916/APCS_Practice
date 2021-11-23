# Method 1
# 接收資料數
number = int(input())
# 迴圈
for i in range(number):
    # 接收資料
    data = input()
    # 轉換字母
    intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    outtab = 'DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc'
    trantab = data.maketrans(intab, outtab)
    # 輸出
    print(data.translate(trantab))


# Method 2
# 接收資料筆數
number = int(print())
# 接收資料
dataList = []
for i in range(number):
    dataList.append(input())

azList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for data in dataList:
    tmp = ''
    # 取出欲加密字串的每個字
    for char in data:
        # 找出字元在列表中的位置
        position = azList.index(char)
        # 將每個字元的位置位移3，並且取出26的餘數
        # newPosition = (position + 3)%26
        newPosition = position-23
        # 取出加密後的文字，存入暫存的變數中
        tmp = tmp + azList[newPosition]
# 輸出每筆資料加密結果
print(tmp)