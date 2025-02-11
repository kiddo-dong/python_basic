# 문자열 자료형
# 문자열 - 문자.단어,등으로 구성된 문자들의 집합

# 파이썬에서 문자열 만드는 방법 4가지.
print("Hello")
print('Hello')
print("""Hello""") # 큰 따음표 3개
print('''Hello''') # 작은 따음표 3개

str_test = '"He"llo' # 변수에 문자열 대입 (따음표로 묶어주어야한다.)
print(str_test)

print("Python's very easy") # 작은 따음표를 문자열 안에서 사용하고 싶다면 큰따음표로 문자열을 묶음
print('"Python is very easy." he says') # 큰 따음표를 문자열 안에서 사용하고 싶다면 작은 따음표로 문자열을 묶음
print("\"Python is very easy.\" he says") # 같은 따음표를 사용하고 싶다면 문자열안의 같은 따음표에 역슬래쉬(\)를 사용

# 여러줄인 문자열 대입
multi_line1= "Life is short\nYou need python" # 두 줄로 이문장을 표현. \n을 사용하여 줄바꿈.
print(multi_line1)

multi_line2 = '''
Hello world
Life is short 
You need python
'''
print(multi_line2) # 위의 \n을 사용하면 가독성이 떨어지므로 작은따음표나 큰따음표 3개를 사용하여 문장을 여러개로 나눌 수 있다.

"""
이스케이프 코드(출력에서 사용)
\n 줄 바꿈
\t 탭 간격
\\ 역슬래시 표현
\' 작은 따옴표 표현
\" 큰 따옴표 표현
\r 커서를 현재줄 가장앞으로 (캐리지 리턴)
\f 커서를 다음줄로 (폼 피드)
\a 부저음 출력(출력시 삑 소리남)
\b 백 스페이스
\000 널문자
"""

print("Hello\nworld!")
print("Hello\t world!")
print("Hello\b world!")
print("Hello\a world")