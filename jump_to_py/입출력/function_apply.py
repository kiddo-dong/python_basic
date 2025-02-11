# 함수를 사용하는 다양한 방법
# 초기값이 있는 매개 변수
# 초기값이 있는 매개 변수는 두가지 방법으로 사용이 가능
def say_myself(name, age, man=True):
    print(f"이름 : {name}")
    print(f"나이 : {age}")
    if man:
        print("남자입니다.")
    else : 
        print('여자입니다.')
 
say_myself('최동현', 23) # 초기값이 True 이므로 생략 시 True 입력
say_myself('최동현', 23, True) # 위와 동일하다

say_myself('최동현', 23, False) # Fale 시 else문 실행 

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 2

vartest(a)
print(a)
# 함수안에서 사용하는 매개변수는 함수 밖의 변수 이름과 전혀 상관 없다.


# 함수안에서 함수 밖의 변수를 변경하는 2 가지방법

# return 사용
# 물론 var_b(b)의 매개변수 b와 이 함수 밖의 b는 완전히 다른 것이다.
b = 1
def var_b(b):
    b = b + 6
    return b
b = var_b(b)
print(b)

# global 명령어 사용
# global 
# 권장하지 않음
c = 1
def c_val():
    global c
    c = c + 8
c_val()
print(c)

# lambdad 예약어 (람다)
# def와 동일한 역할
# 한줄로 간결한 문장일 떄 사용
# 함수명 = lambda 매개변수1, 매개변수2.... : 매개변수를 이용한 표현식

# lambda 예시
add_la = lambda lamb_a, lamb_b : lamb_a + lamb_b
result_la = add_la(3, 4)
print(result_la)
