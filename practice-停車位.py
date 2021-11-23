number = int(input())

for i in range(number):
    data = list(map(int,input().split()))

    resultList = []
    for t in range(data[0]+1,data[1]):
        if t % data[2] != 0:
            resultList.append(t)

    if len(resultList) == 0:
        print('No free parking spaces.')
    else:
        resultList = list(map(str,resultList))
        print(' '.join(resultList))