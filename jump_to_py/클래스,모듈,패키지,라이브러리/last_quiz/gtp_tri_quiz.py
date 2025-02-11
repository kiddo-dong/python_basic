print("1번")
num = 12
result = "Positive" if num > 0 else "Negative"
print(result)

print("2번")
age = 19
result  = "성인" if age >= 18 else "청소년"

print("3번")
a = 12
b = 13
min = a if a < b else b if a == b else b
print(min)

print("4번")
a = 2
b = 9
c = 4
max = a if a > b and a > c else b if b > a and b > c else c
print(max)

print("5번")
score = 80
result ="A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(result)