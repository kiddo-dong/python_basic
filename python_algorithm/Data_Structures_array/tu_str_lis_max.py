# 튜플, 문자열, 문자열 리스트의 최댓값 구하기
from array_max import max_of

tu = (3, 7, 5.6, 2, 3.14, 1)
st = 'string'
arr = ['DTS', 'AAC', 'FLAC']

print(f"튜플의 최댓값 : {max_of(tu)}")
print(f"문자열의 최댓값 : {max_of(st)}")
print(f"문자열 리스트의 최댓값 : {max_of(arr)}")