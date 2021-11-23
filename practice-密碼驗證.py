# 接收資料
data = input()
# 判斷是否全為數字
if data.isdigit():
    # 判斷是否為回文
    copydata = data[::-1]
    if int(data) != int(copydata):
        print('INCORRECT')
        quit()
    else:
        # 判斷後一位是否大於前一位的兩倍
        dataList = list(map(int,data))
        number = len(data)
        for i in range(number-1):
            if (dataList[i])*2 < dataList[i+1]:
                print('INCORRECT')
                quit()
        # 找密碼
        password = ''
        for box in dataList:
            if box % 2 == 0:
                password += str(box)
        if password:
            print(password)
        else:
            print(0)
else:
    print('INCORRECT')
    quit()