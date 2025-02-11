# 이진 검색 알고리즘

# 시간 복잡도 O(log n)
# pl pr pc key값 이용
# 원소 오름차순 입력, 원소 입력시 오름차순이면 break 아닐 시 재입력, 검색 할 값 입력

from typing import Any, Sequence

# 이진 검색 함수 생성
def binary_search(a : Sequence, key : Any) -> int :
    # 배열의 첫번째, 배열의 마지막, 배열의 중앙인덱스 선언
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl+pr)//2

        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == "__main__":
    num = int(input("원소의 개수 입력 : "))
    x = [None] * num

# 배열 원소 오름차순 정렬
    print("배열 데이터를 오름차순으로 입력하세요.")
    x[0] = int(input('x[0] : '))
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f"x[{i}] : "))
            if x[i] >= x[i-1] :
                break
    
    ky = int(input("찾을 값 입력 : "))

    # 이진 검색 함수 호출
    idx = binary_search(x, ky)

    if idx == -1:
        print("찾을 값이 원소에 존재하지 않습니다.")
    else : print(f"검색 값은 x[{idx}]에 있습니다.")

# 복잡도 - 알고리즘의 성능을 객관적으로 평가하는 기준

# 시간 복잡도 - 실행하는데 필요한 시간을 평가
# 공간 복잡도 - 메모리(기억 공간)의 파일 공간이 얼마나 필요한지를 평가