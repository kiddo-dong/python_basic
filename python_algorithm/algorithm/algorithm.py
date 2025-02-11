# 알고리즘 기초

# 알고리즘 - 어떠한 문제를 해결하기 위해 정해놓은 일련의 절차
# 올바른 알고리즘 - 어떠한 경우에도 실행 결과가 똑같이 나오는 것

# 올바른 알고리즘 ex)
def max3(a,b,c):
    max = a
    if b > max : max = b
    if c > max : max = c
    return max # 함수 호출한 문장에 max값 리턴

print(max3(1,3,2)) # 함수 호출
