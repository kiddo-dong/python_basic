# if문
# 조건 판단
# 참과 거짓을 판단해 문장 수행

# if문의 기본 구조
'''
if 조건문 :
    수행문장1
    수행문장2...
else :
    수행문장1
    수행문장2...
'''
# if 문이 true일 경우 if문 안의 수행문장 실행
# if 문이 false일 경우 else안의 수행문장 실행
a = 1
if a == True : # 1은 참이므로 if안의 문장 실행 후 if문을 빠져나옴
    print('참입니다.')
else : 
    print('거짓입니다.')

# else 없이 if문만
money = True
if money: 
    print("참")
print("ㅇ")

# 비교 연산자
'''
x < y 
x > y
x == y
x != y
x >= y
x <= y
'''

# and, or, not 
'''
x or y
x and y
not x
'''
x = False
y = True
print(not x) # T
print(not y) # F 

# in, not in
list_in = [1, 2, 3, 4, 5]
print(3 in list_in) # T
print(7 in list_in) # F
print(3 not in list_in) # F 
print(7 not in list_in)  # T

# ex) 
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print('택시 탑승')
else : 
    print('걸어 가')

print(f'\n{"예시":=^30}\n')

# test_
pock = ['paper', 'cellphone', 'money']
if 'card' in pock:
    print("take a bus")
else : 
    print("go walk")

print(f'\n{"pass 사용":=^30}\n')
# 조건문에서 아무 처리를 하고싶지 않다면
# pass 를 사용
pocket_pass = ['paper', 'cellphone', 'money']
if 'money' in pocket_pass:
    pass
else : 
    ("카드를 꺼내라")


print(f'\n{"elif":=^30}\n')
# elif
# if와 else만으로는 다양한 조건을 판단하기 어려움
# 따라서 elif를 사용하여 조건의 범위를 넓힌다.
'''
if 조건문:
    수행문장1
    수행문장2...
elif 조건문:
    수행문장1
    수행문장2...
elif 조건문:
    수행문장1
    수행문장2
(...생략...)
else :
    수행문장1
    수행문장2
'''
el_poc = ['card', 'paper', 'cellphone']
if 'money' in el_poc:
    print('택시를 타')
elif 'card' in el_poc:
    print('택시 타')
else :
    print('걸어가')


# 조건부 표현식
score = 80
if score >= 60:
    msg = 'success'
else :
    msg = 'faliure'
# 이 대입문을 조건부 표현식으로 간단히 표현이 가능하다.
msg = "success" if score >= 60 else 'faliure'
# 가독성과 활용성이 좋음

