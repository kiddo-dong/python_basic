# 클래스 - 객체를 만드는 틀
# 객체 지향 프로그래밍의 핵심
# 클래스를 정의 하면 그 클래스로 무수히 많은 객체를 생성 가능

# 인스턴스 - 클래스로 만든 객체
# a = cookie() | a는 인스턴스(객체), cookie는 클래스

# 메서드(method) : 클래스 안에 구현된 함수
'''
클래스의 구현방식

class 클래스명 :
    def __init__(그리고 setter매소드):
        속성문장1
        속성문장2 .......

    def 함수명:
        등등...

객체 = 클래스명(__init__속성에 넣을 값)
객체.setter메소드(setter 속성에 넣을 값)
객체.속성
'''

# 클래스 ex)
class cookie : # class cookie 정의
    pass

a = cookie()
b = cookie() # a와 b는 cookie 클래스의 객체(인스턴스)
# 즉, cookie라는 틀로 a와 b의 객체를 cookie 클래스 수행의 리턴값을 저장
# cookie 클래스로 객체를 무한정 만들 수 있음.

# 사칙연산 class
class FourCal : 
    # 필수 조건 속성 메서드 (__init__)
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 선택 조건 속성 메서드 (setter 메서드)
    def setdata(self, first, second): # self, first, second는 메서드 setdata의 매개변수
        self.first = first   # a.first = first(매개변수)
        self.second = second  # a.second = second(매개변수)


    #일반 메서드
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# setdata는 매개변수가 3개이다
# 메소드의 첫 매개변수인 self는 객체 a를 전달한다.(파이썬 클래스의 특징)
# 객체를 호출 할 때 호출한 자기 자신이 전달된다.
a = FourCal(4, 2) # 객체 a
b = FourCal(3, 8) # 객체 b

# setter 메소드인 setdata 사용시 추가로 값 호출 및 선언
# a.setdata(4, 2) # 객체 a에서 setter 메소드 호출. # a.setdata(4, 2) | 호출한 a의 매개변수는 self(파이썬의 특징), 인수 4의 매개변수는 first, 인수 2의 매개변수는 second
# b.setdata(3, 8) # 객체 b에서 setter 메소드 호출

print(f"객체 a : add값 {a.add()} | sub값 {a.sub()} | mul값 {a.mul()} | div값 {a.div()}")
print(f"객체 b : add값 {b.add()} | sub값 {b.sub()} | mul값 {b.mul()} | div값 {b.div()}")

'''
클래스 정리
클래스 - 객체를 생성하는 틀
인스턴스 - 클래스로 생성한 객체

__init__ 속성 메소드 - 클래스에서 필수 속성을 정의
인스턴스 생성과 동시에 호출
인스턴스 = 클래스명(속성 값)
setter 속성 메소드 - 클래스에서 필요한 객체만 사용하는 속성을 정의
인스턴스 = 클래스명()
인스턴스명.setter속성메소드명(속성값)
'''
