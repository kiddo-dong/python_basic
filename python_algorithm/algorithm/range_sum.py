# a부터 b 까지 정수의 합

a = int(input("정수 a 입력 : "))
b = int(input("정수 b 입력 : "))

if a > b :
    a, b = b, a # a = b , b = a

sum = 0 
for i in range(a,b+1):
    sum+=i
print(sum)