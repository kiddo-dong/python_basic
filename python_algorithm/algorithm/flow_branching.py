# 조건문과 분기
# 흐름의 분기

# 분기 - 프로그램의 실행 흐름을 다른곳으로 변경하는 명령을 뜻함.

# 3개의 분기
n = 17  # int(input('정수를 입력하세요 : '))
if n > 0 :
    print("양수")
elif n < 0 :
    print("음수")
else :
    print("0입니다.")

# 4개의 분기
num = int(input("정수를 입력하세요 : "))
if num == 1:
    print('A')
elif num == 2 :
    print('B')
elif num == 3:
    print('C')
# num이 1,2,3 일때 분기 3개와 그 이외의 수가 입력되었을때의 경우 1개로
# 총 4개의 분기
# else : pass 가 포함되어있음
else : pass
# else 문이 까지 분기 4개

# 연산자
'''
단항 연산자 : -a
이항 연산자 : a < b
삼항 연산자 : a if b else c
'''
