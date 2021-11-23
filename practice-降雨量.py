totalList = []
morning = 0
afternoon = 0
night = 0
early = 0

for i in range(7):
    data = list(map(float,input().split()))
    total = 0
    for t in range(4):
        total += data[t]
    totalList.append(total)
    morning += data[0]
    afternoon += data[1]
    night += data[2]
    early += data[3]

day = totalList.index(max(totalList)) + 1
print(day)

timeList = []
timeList.append(morning)
timeList.append(afternoon)
timeList.append(night)
timeList.append(early)
dayList = ['morning','afternoon','night','early morning']
time = dayList[timeList.index(max(timeList))]
print(time)