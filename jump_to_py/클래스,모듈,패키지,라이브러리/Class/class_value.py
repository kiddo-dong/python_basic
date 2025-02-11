# 클래스 변수
# 객체 변수와 달리 클래스로 만든 모든 객체(인스턴스)에 공유가됨.
'''
class 클래스명:
    클래스_변수명 = Value

클래스명.클래스변수명

'''
class Family:
    lastname = "박" # 클래스변수 선언

print(Family.lastname) # 클래스변수 사용

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

a.lastname = "최" # a 객체에 lastname이라는 객체변수 생성
print(a.lastname) # Family의 클래스변수와 동일한 이름이지만 a의 객체변수이다. (이름만 동일)
print(Family.lastname) # 클래스변수
print(b.lastname) 
a = Family()
print(a.lastname)