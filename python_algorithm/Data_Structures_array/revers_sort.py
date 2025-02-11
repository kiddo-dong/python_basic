# 뮤터블 시퀀스 원소 역순 정렬

from typing import Any, MutableSequence

def re_sort(a : MutableSequence) -> Any :
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == "__main__" :
    print("원소 배열 역순 정렬")
    nx = int(input("원소 수를 입력 : "))
    x = [None] * nx

    for i in range(nx) :
        x[i] = int(input(f"x[{i}] 의 값 입력 : "))
        
    re_sort(x)
    print("배열 원소 역순 정렬 완료")

    for i in range(nx):
        print(f'x[{i}] = {x[i]}')