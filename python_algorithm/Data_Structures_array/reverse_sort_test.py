# 뮤터블 시퀀스 원소 배열 역순 정렬
# 갯수 및 배열원소 입력 받기

from typing import Any, MutableSequence

# a = 리스트 7
def rev_sort(a : MutableSequence) -> Any:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == "__main__":
    print("뮤터블 시퀀스 원소 배열 역순 정렬")
    num = int(input("배열의 길이 입력 : "))
    num_list = [None] * num # 배열의 길이만큼 인덱스 생성
    
    for i in range(num):
        num_list[i] = int(input(f"x[{i}] 값 입력 : "))

    rev_sort(num_list)
    print("정렬 완료")

    for i in range(num):
        print(f'x[{i}] = {num_list[i]}')