# try-else 문
# try 문에서 오류가 발생하지 않으면 else 절이 실행된다.
# 오류 발생 시 except 절 실행
'''
try :
    ....
except [발생오류 [as 오류변수]] :
    ....
else :          # 오류가 없을 경우에만 실행
    ....
'''

# ex)
try:
    age = int(input("나이를 입력하세요 : "))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else :
        print("환영합니다.")
