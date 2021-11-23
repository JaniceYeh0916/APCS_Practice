apple = list(map(int,input().split()))
high = int(input())

number = 0

for i in range(len(apple)):
    if high + 30 >= apple[i]:
        number +=1

print(number)