# 선형 검색 알고리즘
# 갯수 입력, 원소 입력, 검색 값 입력, 총 출력

# for문 사용
from typing import Any, Sequence

def linear_search(a : Sequence, key : Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == "__main__":
    num = int(input("원소 갯수 입력 : "))
    x = [None] * num

    for i in range(num):
        x[i]= int(input(f"원소값 입력 x[{i}] : "))

    ky = int(input("검색값 입력 : "))

    idx = linear_search(x, ky)

    if idx == -1:
        print("검색값이 원소에 존재하지 않음")
    else: print(f"검색값은 x[{idx}]에 있습니다.")