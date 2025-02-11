# 스택(stack)
# 후입 선출 (LIFO)

# 구조
# push - 스택에 데이터를 넣는 작업
# pop - 스택에서 데이터를 꺼내는 작업
# top - push 와 pop을 하는 윗부분
# bottom - 스택의 밑 부분

# 스택 - push와 pop 과정(후입선출)
'''
5:push   7:push   pop      pop
| |      | |      | |      | |
| |      |7|      | |      | |
|5|      |5|      |5|      | |
|-|      |-|      |-|      |-|

'''

# 스택 구현

# 01. ============================================================
# 스택 배열(stk) - 푸시한 데이터를 저장하는 스택 본체 list형 배열

# 스택 크기(capacity) - 스택에 쌓을 수 있는 데이터의 최대 갯수

# 스택 포인터(ptr) - 스택에 쌓여있는 데이터의 갯수

# 예외 처리 클래스(Empty) - pop() 또는 peek() 호출 시 스택이 비어있으면 내보내는 예외처리

# 예외 처리 클래스(Full) - push() 호출 시 스택이 가득 차있으면 내보내는 예외 처리

# __init__() 함수 - 스택 초기화 (매번 새 객체마다 초기화 후 메소드에서 이용됨)

# __len__()- 스택에 쌓여있는 개수 반환
# 스택 포인터 ptr값을 그대로 반환

# is_empty() - 스택이 비어있는지 확인 True, False
# is_full() - 스택이 가득 차 있는지 확인 True, False

# 02. ============================================================
# push() - 스택에 데이터를 추가 - full의 예외처리
# pop() - 스택 탑에서 데이터를 꺼내 반환 - empty의 예외처리
# peek() - 스택 탑 데이터 스캔 (다음에 pop()할 데이터) - empty의 예외처리 | 데이터가 있다면 stk[ptr - 1]

#03. =============================================================
# clear() - 스택의 모든 데이터를 삭제ㄴㄴㄴ
# find() - 데이터를 검색 하는 find 함수
# count() - 값이 스택에 존재하는 개수수
# # __contains__() - 스택에 데이터가 있는지 판단(True, False) 판단 연산자 in 사용가능
# dump() - 스택에 쌓여있는 모든 데이터를 바텀부터 탑까지 순서대로 출력 | 스택이 비어있다면 '스택이 비어있습니다.' 출력


# FixedStack 알고리즘
from typing import Any
# 01
class FixedStack:
    # 빈 스택 예외처리
    class Empty(Exception):
        pass
    
    # 풀 스택 예외처리
    class Full(Exception):
        pass
    
    # 속성 초기화 및 선언
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    # 스택 포인터의 크기
    def __len__(self) -> int:
        self.ptr
    
    # 빈 스택 판단
    def is_empty(self) -> bool:
        return self.ptr <= 0
    
    # 풀 스택 판단
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
# 02
    # 데이터를 스택에 push()
    def push(self, value: Any)-> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = valuen
        self.ptr += 1
    
    # 데이터를 스택에서 pop()
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    # 스택 데이터 스캔(다음에 pop() 할 데이터) empty 시 예외 처리
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
# 03
    # 스택을 비움(모든 데이터 삭제) 
    def clear(self) -> None:
        self.ptr = 0

    # 검색 값 찾는 find()
    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    # 스택에 있는 값의 개수를 반환
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    # 스택에 값이 있는지 판단
    def __contains__(self, value: Any) -> bool :
        return self.count(value) > 0
    
    # 덤프(스택 안의 모든 데이터를 바텀부터 탑까지 츨력)
    def dump(self) -> None:
        if self.is_empty():
            print("스택이 비어있습니다.")
        else: 
            print(self.stk[:self.ptr])