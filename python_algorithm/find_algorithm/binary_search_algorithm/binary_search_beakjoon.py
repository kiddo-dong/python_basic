# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

from typing import Sequence,Any
import sys
input = sys.stdin.readline

N = int(input())
K = list(map(int,input().split()))

M = int(input())
L = list(map(int,input().split()))


def binary_search(a: Sequence, key: Any, pl, pr)-> int :
    while pl <= pr:
        pc = (pl + pr) // 2
        
        if a[pc] == key:
            return print("1")
        elif a[pc] < key:
            pl = pc + 1
        else : pr = pc - 1
    return print("0")

if __name__ == "__main__":
    print(binary_search(N, K, 0, len(N)-1))
    print(binary_search(M, L, 0, len(M)-1))