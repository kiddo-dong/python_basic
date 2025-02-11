# 알고리즘 기초
# max_value.py 세 정수의 최댓값을 함수로 구현

def max3(a,b,c):

    max = a
    if b > max : max = b
    if c > max : max = c
    return max

print(max3(1,3,2))