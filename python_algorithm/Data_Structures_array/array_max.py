# 배열 원소 최댓값 구하기
'''
# 배열 최댓값 함수
def max_of(a):
    maximum = a[0]
    for i in range(1, len((a))):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
'''

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print("최댓값을 구함")
    num = int(input("원소 수를 입력 : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력 : '))
    
    print(f"최댓값은 : {max_of(x)}")

# 알고리즘 용어
# 스캔 - 배열 원소를 하나하나 차례로 살펴보는 방식