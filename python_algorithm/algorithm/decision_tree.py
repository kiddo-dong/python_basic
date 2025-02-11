# 결정 트리
# 데이터를 기반으로 한 의사 결정 과정을 시각적으로 트리 구조로 표현

# 세 정수를 입력받아 중앙값 구하기 1
def med3(a, b, c):
    # a,b,c 의 중앙값을 구하여 return
    if a >= b:
        if b >= c:
            return b
        elif b <= c:
            return c
        else : return a
    elif a > c:
        return a
    elif b > c :
        return c
    else :
        return b
    
print(f"세 정수의 중앙값 : {med3(1,3,2)}")
print(f"세 정수의 중앙값 : {med3(4,45,13)}")

# 위 의 결정 트리에 비해 효율적이지 못함.
def med_other3(a, b, c):
    if (a >= b and a <= c) or ( b >= a and a >= c):
        return a
    elif (b > a and b < c) or (c > b and a < b):
        return b
    else: return c

print(f"세 정수의 중앙값 : {med_other3(1,3,2)}")
print(f"세 정수의 중앙값 : {med_other3(4,45,13)}")