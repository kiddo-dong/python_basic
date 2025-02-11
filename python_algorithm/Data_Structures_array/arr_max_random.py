# 배열 원소 난수 최댓값 구하기 
from array_max import max_of
import random

print("난수의 최댓값을 구합니다.")
number = int(input("생성할 난수의 갯수 : "))
first = int(input("난수의 최솟값 : "))
last = int(input("난수의 최댓값 : "))

# x = [] 빈 리스트 (아무 요소 없음)	0
# x = [None] 리스트에 None 값이 하나 들어 있음 1
x = [None] * number

for i in range(number):
    x[i] = random.randint(first,last)

print(x)
print(f"난수의 최댓값 [{max_of(x)}]")