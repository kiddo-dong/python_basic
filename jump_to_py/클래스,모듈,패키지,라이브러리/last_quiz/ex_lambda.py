print("1번")
a = [1,2,3,4,5]
print(lambda a : a ** 2)

print("2번")
print(list(map(lambda a: a + 10, a)))

print("3번")
print(list(map(lambda a,b=10 : a + b, a )))

print("4번 오류수정")
a = [1, 2, 3, 4, 5]
b = 10
result = list(map(lambda a,b : a+b, a))  # 오류 발생