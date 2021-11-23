# 磁力蜈蚣

# 輸入
# 5 (資料長度)
# 99 77 66 44 11 (資料)
# 輸出
# 99 77 66 44 11 
# 11 44 66 77 
# 77 66 44 
# 44 66 
# 66

# 接收資料
dataLength = input('')
data = input('')

# 99 77 66 44 11 利用空格切開
dataSplit = data.split(' ')
print(' '.join(dataSplit))

# 迴圈
for i in range(int(dataLength)-1):
    # 反轉 reverse()
    dataSplit.reverse()
    # 丟掉最後一個 pop()
    dataSplit.pop()
    # 以數列呈現 '分隔符號'.join()
    print(' '.join(dataSplit))