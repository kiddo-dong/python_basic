# 선형 검색 알고리즘
# 배열 검색의 가장 기본적인 알고리즘

# 선형 검색 - 직선 모양(선형)으로 늘어선 배열에서 검색하는 경우에 원하는 키 값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘
# 순차검색이라고 하기도 함.

# 선형 검색 (while문)
from typing import Any, Sequence

def seq_serch(a : Sequence, key : Any) -> int:
    i=0
    while True:
        if i == len(a):
            return -1
        if a[i] == key :
            return i
        i+=1

if __name__ == "__main__":
    num = int(input("원소 갯수 입력 : "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))
    
    ky = int(input("검색 할 값을 입력 : "))

    idx = seq_serch(x, ky)

    if idx == -1 :
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else :
        print(f"검색값은 x[{idx}]에 있습니다.")