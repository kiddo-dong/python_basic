# 여러개의 오류 처리하기

# try 문 안에서 여러 개의 오류를 처리
'''
try :
    ....
except 발생오류1 :
    ....
except 발생오류2 :
    ....

'''
# ex)
'''
try :
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없다.")

except IndexError :
    print("인덱싱 불가능")
'''
# IndexError 에러가 먼저 나기 떄문에 except INdexError 문이 실행이 된다.

# e 변수에 넣어보기
'''
try :
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e :
    print(e)
except IndexError as e :
    print(e)
'''

# except 하나로 묶기
try :
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e :
    print(e)