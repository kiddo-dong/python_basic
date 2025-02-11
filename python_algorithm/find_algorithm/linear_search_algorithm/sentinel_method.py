# 보초법

# 선형 검색에서의 높은 검사 비용을 반으로 줄일 수 있음.
# 시퀀스의 마지막 인덱스 뒤에 검색 값을 추가하여 값을 비교

from typing import Any, Sequence
from copy import deepcopy

def seq_search(seq : Sequence, key : Any) -> int:
    a = deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i]==key:
            break
        i+=1
        return -1 if a[i]==len(seq) else i
    

if __name__ == "__main__" :
    num = int(input("원소 갯수 입력 : "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f" x[{i}] : "))
    
    ky = int(input("검색 할 값 입력 : "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 없음")
    else:
        print(f"검색 값은 x[{idx}]에 존재")