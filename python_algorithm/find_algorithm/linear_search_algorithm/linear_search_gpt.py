# 문제 1 : 기본 선형 검색
'''
from typing import Any, Sequence

def linear_search(seq : Sequence, key : int) -> int :
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return -1

if __name__ == "__main__":
    num = int(input("정수 배열의 크기입력 : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"원소 값 입력(정수) x[{i}] : "))

    ky = int(input("찾을 값 입력(정수) : "))

    idx = linear_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else : print(f"검색값은 x[{idx}]에 있습니다.")
'''

# 문제 2: 검색할 값이 여러 개인 경우
'''
from typing import Any, Sequence

def linear_search_multi(seq: Sequence, key : int) -> list:
    id_list = []
    for i in range(len(seq)):
        if seq[i] == key:
            id_list.append(i)
    return -1 if not id_list else id_list

if __name__ == "__main__" :
    num = int(input("정수 배열의 크기입력 : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"원소 값 입력(정수) x[{i}]: "))
        
    ky = int(input("찾을 값 입력(정수) : "))

    idx = linear_search_multi(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else : print(f"검색값은 x{idx}에 있습니다.")
'''

# 문제 3: 보초법을 이용한 선형 검색
from typing import Any, Sequence

def sentinel_method(seq : Sequence, key : int) -> int :
    seq.append(key)    
    
    i=0
    while True:
        if seq[i] == key:
            break
        i += 1
    seq.pop()

    return -1 if i == len(seq) else i


if __name__ == "__main__" :
    num = int(input("정수 배열의 크기입력 : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"원소 값 입력(정수) x[{i}]: "))
        
    ky = int(input("찾을 값 입력(정수) : "))

    idx = sentinel_method(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else : print(f"검색값은 x[{idx}]에 있습니다.")

'''
# 도전문제: 문자열 배열에서 검색
from typing import Any, Sequence

def linear_search(seq : Sequence, key : str) -> int:
    for i in range(len(seq)):
        if seq[i] == key:
            return i
    return -1

if __name__ == "__main__" :
    num = int(input("문자열 배열의 크기입력 : "))
    x = [None] * num

    for i in range(num):
        x[i] = str(input(f"각 문자열 입력(문자열) x[{i}]: "))
        
    ky = str(input("찾을 값 입력(문자열) : "))

    idx = linear_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else : print(f"검색값은 x[{idx}]에 있습니다.")
'''