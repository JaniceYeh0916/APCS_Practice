try:
    data = list(map(int,input().split()))

    box = []
    for i in range(1,data[0]+1):
        box.append(data[i])

    from itertools import permutations
    element = list(map(str,permutations(box,data[0])))

    elementList = []
    for t in range(len(element)):
        boxList = list(element[t])
        boxList.remove('(')
        boxList.remove(')')
        for i in boxList:
            if i == ',':
                boxList.remove(i)
            if ' ' in boxList:
                boxList.remove(' ')
        elementList.append(''.join(boxList))
    resultList = list(map(int,elementList))

    print(resultList[len(element)-1])
except:
    pass
