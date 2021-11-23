data = list(map(int,input().split()))

result = 0

for i in range(1,data[2]+1):
    if i % data[0] == 0:
        result += i
    elif i % data[1] == 0:
        result += i
    else:
        result += 0

while result > 26:
    result -= 26

charList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

char = charList[result - 1]
print(char)
