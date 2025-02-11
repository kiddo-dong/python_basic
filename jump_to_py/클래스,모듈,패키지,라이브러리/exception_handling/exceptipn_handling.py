# 예외 처리
# 프로그램 제작 중 발생하는 다양한 오류로 프로그램이 잘못 동작하는 것을 막기 위한 것

# 오류 예외 처리 기법

# try-except
"""
try:
    ...
except [발생오류 [as 오류변수]]:    # [] 생략 가능한 문장
    ...
"""
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
# try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

# 1. try-except만 쓰는 방법
'''
try :
    ...
except :
    ...
'''
# 2. 발생 오류만 포함한 except문
'''
try : 
    ...
except 발생오류 :
    ...
'''
# 3. 발생오류와 오류변수까지 포함한 except문
'''
try :
    ...
except 발생오류 as 오류변수 :
    ...
'''

# ex)
try :       # try 문이 오류가 발생하면 except문 실행 
    4/0
except ZeroDivisionError as e : # ZeroDivisionError가 발생하면 변수 e 에 오류 메시지를 담음
    print(e) # 



