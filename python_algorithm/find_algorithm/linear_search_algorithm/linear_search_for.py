# 선형 검색 알고리즘 (for 문)
# 갯수 입력 받기, 원소 입력받기, 검색할 key입력받기

from typing import Any, Sequence

def linear_serch(a : Sequence, key : Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == "__main__" :

    # 변수 선언 및 배열 원소 값 부여
    num = int(input("원소 개수를 입력 : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"원소 입력 x[{i}] : "))
    
    ky = int(input("검색할 값을 입력 : "))

    # 선형 검색 함수 호출
    idx = linear_serch(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지않음")
    else : 
        print(f"검색값은 x[{idx}]에 있습니다.")

    # 선형 검색은 데이터가 많아질 수록 시간복잡도 O(n)가 올라감.
    # 데이터가 작은 규모일때 사용
    # 데이터가 정렬되고, 많을 시 이진 검색 사용 | 이진검색 시간 복잡도 O(log n)

