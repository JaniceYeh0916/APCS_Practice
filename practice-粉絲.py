data = list(map(int,input().split()))

numberList = []
for i in range(data[0]):
    numberList.append([i,int(0)])
for i in range(data[1]):
    box = list(map(int,input().split()))
    numberList[box[0]][1] += box[1]

notZeroList = []
for i in range(data[0]):
    if numberList[i][1] != 0:
        notZeroList.append(numberList[i])

new = []
for i in range(len(notZeroList)):
    c = notZeroList[i][::-1]
    new.append(c)

notZeroListMax = sorted(new,reverse = True)
for i in range(len(notZeroListMax)):
    ans = list(map(str,notZeroListMax[i]))
    ans = ans[::-1]
    print(' '.join(ans))
    ans = list(map(int,ans))
    numberList.remove(ans)

for i in range(len(numberList)):
    ans = list(map(str,numberList[i]))
    print(' '.join(ans))
