# 함수
'''
def 함수명(매개 변수):
    수행문장1
    수행문장2
'''
# def
def fon_name(a, b): # def 로 함수정의, 함수명은 fon_name, 매개변수는 a, b 두개
    return a + b    # a + b의 결과 값을 return 해준다.

x = 3
y = 4
c = fon_name(x, y)
print(c)

# 매개변수와 인수
# 매개 변수와 인수는 같이 사용하는 용어이다.
# 매개 변수 - 함수의 입력으로 전달된 값을 받는 변수
# 인수 - 함수를 호출할때 입력값

def add(a, b): # <- a, b는 매개 변수
    return a + b
print(add(5,10)) # <- 5, 10은 인수

# 일반적인 함수
"""
def 함수명(매개변수):
    수행문장1
    수행문장2
    .....
    return 리턴값
"""
# 리턴 받을 변수 = 함수명(인수1, 인수2, ...)
def add_def(ad_a, ad_b): # <- ad_a, ad_b 매개변수
    result = ad_a + ad_b
    return result

a_sum = add(3, 4) # <- 3, 4 인수
print(a_sum)


# 입력값이 없는 함수
# 리턴 받을 변수 = 함수명()
def str_de():
    return 'Hi'

a = str_de()
print(a)

# 리턴값이 없는 함수
# 함수명(인수1, 인수2)
def nore(a, b):
    print(f"{a}, {b}의 합은 {a+b}입니다.")
nore(10, 20)
re = nore(1,2)
print(re)
# 리턴값이 없으므로 리턴값을 대입받은 re변수가 None이 나온다.


# 입력값도, 리턴값도 없는 함수
# 함수명()
def say():
    print('Hi')
say()


# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b
sub_re = sub(a=5, b=3) # (b=3,a=5) 매개변수 위치를 변경해도됨.
print(sub_re)


# 여러개의 입력값을 받는 함수
'''
def 함수명(*매개 변수)
    수행문장
    수행문장...
'''
def add_many(*abcd):
    result = 0
    for i in abcd:
        result+=i
    return result

print(add_many(1,2,3))
print(add_many(1,2,3,4,5,6,7,8,9,10))

# 여러개의 입력값을 받는 함수 (매개변수 여러개)
# 매개 변수에 *
# 리스트나 튜플이면 인자에도 *를 붙여준다.
# def 함수명(*매개 변수)
def add_mul(choice, *yay):
    if choice == "add":
        result = 0
        for i in yay:
            result += i
    elif choice == "mul":
        result = 1
        for i in yay:
            result *= i
    return result

print(add_mul("add",1,2,3,4,5))
print(add_mul("mul",1,2,3,4,5))

'''
# ex) 팩토리얼 함수를 만들어보자
print(f"\n{'팩토리얼':=^30}\n") 

def pac(pac_num):
    pac_result = 1
    for i in range(1, pac_num + 1):
        pac_result = pac_result * i
    return pac_result

pac_in = input("팩토리얼 계산입니다.\n원하는 팩토리얼 수를 입력하세요 : ")
if pac_in.isdigit():
    pac_in = int(pac_in)
    print(pac(pac_in))
else :
    print("정수가 아닙니다 정수를 입력하세요.")
'''

'''
# ex)입력받은 수들을 더하는 프로그램
def num_sum(*number):
    res_sum = 0
    for i in number:
        res_sum += i
    return res_sum
numint = list(map(int,input("더할 일의자리 수를 연속 입력하세요 : ")))
print(num_sum(*numint))
'''


# 키워드 매개변수, kwargs
# 매개 변수에 **
# def 함수명(**매개 변수)
def key_wag(**keys):
    return keys
print(key_wag(a = 1, b = 2))
# 키워드 매개변수로 딕셔너리를 만들 수 있다.


# 리턴 값은 하나만 존재
# 리턴 값은 하나만 존재하므로 튜플로 리턴 받기
def add_and_mul(a, b):
    return a + b, a * b
re_ad_mu = add_and_mul(3, 4)
print(re_ad_mu)
# re_ad_mu 변수는 리턴값으로 튜플이 나온다.

# 튜플이 아닌 두개의 값으로 분리하여 리턴받기
def add_double(a, b):
    return a + b, a * b

dou1, dou2 = (add_double(3, 4))
print(f'리턴 값 1 : {dou1}')
print(f'리턴 값 2 : {dou2}')

# 리턴 값을 dou1, dou2로 분리해서 리턴을 받을 수 있다.

# 함수는 return문을 만나는 순간 return값을 돌려준 다음 함수를 빠져나간다.

