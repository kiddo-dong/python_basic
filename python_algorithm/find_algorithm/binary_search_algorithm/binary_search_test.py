# 이진 검색 알고리즘

# 시간 복잡도 O(log n)
# pl pr pc key값 이용
# 원소 오름차순 입력, 원소 입력시 오름차순이면 break 아닐 시 재입력, 검색 할 값 입력

from typing import Any, Sequence

def binary_search(a : Sequence, key : Any) -> int:
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl+pr) // 2
        if x[pc] == key:
            return pc
        elif x[pc] < key:
            pl = pc + 1
        else : 
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == "__main__" : 
    num = int(input("원소 갯수 입력 : "))
    x = [None] * num

    print("원소를 오름차순으로 입력하세요.")
    x[0] = int(input("x[0] : "))

    #오름차순이 아닐 시 원소 재입력
    for i in range(1,num):
        x[i] = int(input(f"x[{i}] :"))
        while True:
            if x[i] >= x[i-1]:
                break
    
    ky = int(input("검색 값 입력 : "))

    idx = binary_search(x, ky)
    
    if idx == -1:
        print("검색 값이 원소에 존재하지않음")
    else : print(f"검색값은 x[{idx}]에 있습니다.")