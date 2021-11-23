# 接收資料
number = int(input())
data = list(map(int,input().split()))
data.sort()

# 將最大的兩個數字提出
big = data.pop()
small = data.pop()

# 分配剩下的數字
data.reverse()

index = 0
for i in data:
    if index % 2 ==0:
        small = small * 10 +i
    else:
        big = big * 10 +i
    index += 1

print(big*small)
