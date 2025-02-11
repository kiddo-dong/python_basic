# 1-n까지 정수의 합

sum = 0

while True :
    n = int(input("n 값 입력 : "))
    if n > 0 :
        break

for i in range(1, n+1):
    sum += i
print(sum)