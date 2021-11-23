number = int(input())
time = list(map(int,input().split()))
middleList = []
for i in range(number):
    middle = int(input())
    middleList.append(middle)
stopList = list(map(int,input().split()))

for k in range(len(stopList)-1):
    hour = time[0]
    minute = time[1]
    for t in range(stopList[k]):
        minute += middleList[t]
    while minute >= 60:
        minute -= 60
        hour += 1
    while hour >= 24:
        hour -= 24
    if hour < 10 and minute < 10:
        print('0'+ str(hour) + ':' +'0'+ str(minute))
    elif hour < 10 and minute >= 10:
        print('0'+ str(hour) + ':' + str(minute))
    elif hour >= 10 and minute < 10:
        print(str(hour) + ':' + '0'+ str(minute))
    else:
        print(str(hour) + ':' + str(minute))
