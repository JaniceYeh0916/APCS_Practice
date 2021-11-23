data = list(map(int,input().split()))

n = data[0]
m = data[1]
for i in range(2,n+1):
    while(n%i==0 and m%i==0):
        n=n//i
        m=m//i

day = 0
number = n + m
while number > 1:
    number /= 2
    day += 1

print(day)