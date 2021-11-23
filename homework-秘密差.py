data = input()
print(list(data))

index = 0
A = 0
B = 0
for i in data:
    if index % 2 == 0:
        print('偶數位',i)
        B += int(i)
    else:
        print('奇數位',i)
        A += int(i)
    index += 1
print(abs(A-B))