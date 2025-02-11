#문제 1: 기본 이진 검색

'''
from typing import Any,Sequence

def binary_search(a: Sequence, key : Any) -> int :
    pl = 0
    pr = len(a) - 1

    while pl <= pr:
        pc = (pl+pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else: pr = pc - 1

    return -1

def my_search():
    num = int(input("원소 개수 입력 : "))
    x = [None] * num

    print("원소 오름차순 입력")
    x[0] = int(input("x[0] : "))

    for i in range(1, num):
        while True : 
            x[i] = int(input(f"x[{i}] : "))
            if x[i] >= x[i-1]:
                break
    return x

if __name__ == "__main__" :
    
    x = my_search()
    ky = int(input("검색값 입력 : "))
    
    idx = binary_search(x, ky)
    
    if idx == -1:
        print("검색값이 존재하지않음")
    else: print(f"검색값은 x[{idx}]에 있음")
'''

#문제 2: 여러 개의 중복된 값
'''
from typing import Any,Sequence

def binary_search(a : Sequence, key: Any) -> int :
    pl = 0
    pr = len(a) - 1
    ad = []
    
    while pl <= pr:
        pc = (pl + pr) // 2
        if a[pc] == key:
            # 검색된 값의 인덱스를 저장
            ad.append(pc)
            # 좌우로 확장하여 중복된 값을 확인
            left = pc - 1
            right = pc + 1
            while left >= 0 and a[left] == key:
                ad.append(left)
                left -= 1
            while right < len(a) and a[right] == key:
                ad.append(right)
                right += 1
            break
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
    return sorted(ad) if ad else -1

def my_search():
    num = int(input("원소 갯수 입력 : "))
    x = [None] * num

    print("원소를 오름차순으로 입력")
    x[0] = int(input("x[0] : "))

    for i in range(1, num):
        while True:
            x[i] = int(input(f"x[{i}] : "))
            if x[i] >= x[i-1]:
                break
            print("오름차순이 아님 다시입력하세요.")
    return x

if __name__ == "__main__":
    x = my_search()

    ky = int(input("검색값 입력 : "))

    idx = binary_search(x,ky)

    if idx == -1 :
        print(f"검색값 {ky}는 원소에 존재하지 않음")
    else : print(f"검색값 {ky}는 x{idx}에 존재함")
'''
'''
#문제 3: 내림차순 배열에서 이진 검색
from typing import Sequence, Any
def binary_search(a : Sequence, key : Any) -> int:
    pl = 0
    pr = len(a)-1

    while pl <= pr :
        pc = (pl + pr) // 2
        if a[pc] == key :
            return pc
        elif a[pc] < key:
            pr = pc - 1
        else: pl = pc + 1
    return -1

def my_search():
    num = int(input("원소 개수 입력 : "))
    x = [None] * num

    print("내림차순으로 입력 : ")
    x[0] = int(input("x[0] : "))
    for i in range(1, num):
        while True:
            x[i] = int(input(f"x[{i}] : "))
            if x[i] <= x[i-1]:
                break
            print("내림차순 입력이 아님. 다시 입력하세요.")    
    return x

if __name__ == "__main__":

    x = my_search()

    ky = int(input("검색 값 입력 : "))

    idx = binary_search(x, ky)

    if idx == -1 : 
        print(f"검색값 {ky}는 원소에 없습니다.")
    else:
        print(f"검색값 {ky}는 x[{idx}]에 있습니다.")
'''
# 문제 4: 문자열 배열 이진 탐색 알고리즘
'''
from typing import Sequence

def binary_search_str(a : Sequence, key : str) -> int:
    pl = 0
    pr = len(a) - 1

    while pl <= pr :
        pc = (pl + pr) // 2
        
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else : pr = pc - 1
    return -1

def my_str():
    num = int(input("원소 갯수 입력 : "))
    x = [None] * num

    print("문자열을 오름차순으로 입력")
    x[0] = input("x[0] : ")

    for i in range(1, num):
        while True:
            x[i] = input(f"x[{i}] : ")
            if x[i] >= x[i-1]:
                break
            print("잘못 입력하셨습니다. 재 입력하세요")

    return x

if __name__ == "__main__":
    x = my_str()
    ky = input("검색값 입력 : ")
    
    idx = binary_search_str(x, ky)

    if idx == -1:
        print(f"검색 값 {ky}가 원소에 존재하지 않음")
    else : print(f"검색 값 {ky}는 x[{idx}]에 있습니다.")

'''
# 문제 5: 값이 없는 경우 가장 가까운 위치 찾기
from typing import Any, Sequence

def binary_search(a : Sequence, key : Any) -> int :
    pl = 0
    pr = len(a)-1

    while pl <= pr :
        pc = (pl + pr) // 2

        if a[pc] == key:
            return pl, pr, pc
        elif a[pc] < key:
            pl = pc + 1
        else: pr = pc -1

    return pl, pr, -1


def my_search() -> Sequence[int]:
    num = int(input("원소 개수 입력 : "))
    x = [None] * num

    print("원소를 오른차순으로 입력")
    x[0] = int(input("x[0] : "))

    for i in range(1, num):
        while True :
            x[i] = int(input(f"x[{i}] : "))
            if x[i] >= x[i-1]:
                break
            print("오름차순 입력이 아님, 재입력")
    return x

if __name__ == "__main__" :
    x = my_search()
    ky = int(input("검색 값 입력 : "))

    result = binary_search(x, ky)
    if isinstance(result, int):
        print(f"검색 값은 {ky}는 x[{result}]에 있습니다.")
    else :
        pl, pr, _ = result
        if pr < 0:
            print(f"가장 가까운 값은 x[{pl}] ({x[pl]})에 있습니다.")
        elif pl >= len(x):
            print(f"가장 가까운 값은 x[{pr}] ({x[pr]})에 있습니다.")
        else:
            # pl과 pr 중 더 가까운 값 판단
            nearest = pl if abs(x[pl] - ky) < abs(x[pr] - ky) else pr
            print(f"가장 가까운 값은 x[{nearest}] ({x[nearest]})에 있습니다.")