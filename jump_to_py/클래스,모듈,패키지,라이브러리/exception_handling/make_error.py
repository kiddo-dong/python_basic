# 예외(에러) 만들기
# 특수한 경우 예외 처리를 할려고 예외(오류)를 만들어서 사용을한다.

# 내장 클래스 Exception 클래스 상속
class MyError(Exception):
    pass
    # 오류메시지를 사용하고싶을때
    '''
    def __str__(self):
        return "허용되지 않는 별명입니다."
    '''

def say_nick(nick):
    if nick == "바보" :
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명")

# 오류 메시지를 사용하고 싶을 때
'''
except MyError as e:
    print(e)
'''
