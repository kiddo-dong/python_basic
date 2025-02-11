#  a부터 b까지 더하기 조건 판단

a = int(input("정수 a입력 : "))
b = int(input("정수 b입력 : "))
sum = 0

if a > b :
    a, b = b, a
for i in range(a,b+1):
    if i < b :
        print(f" {i} +", end ="")
    else :
        print(f" {i} =", end = "")
    sum += i
print(f" {sum}")