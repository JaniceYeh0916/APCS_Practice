data = list(map(int,input().split()))

number = data[1] // 1000

CPList = []
numberList = []
for i in range(data[0]):
    pet = list(map(int,input().split()))
    if 0 <= pet[1] <= 29:
        CP = pet[0] + 10 * number
    elif 30 <= pet[1] <= 39:
        CP = pet[0] + 50 * number
    elif 40 <= pet[1] <= 49:
        CP = pet[0] + 100 * number
    CPList.append(CP)
    numberList.append(i+1)

CPList2 = sorted(CPList,reverse=True)
char = numberList[CPList.index(CPList2[0])]
print(char,CPList2[0])
