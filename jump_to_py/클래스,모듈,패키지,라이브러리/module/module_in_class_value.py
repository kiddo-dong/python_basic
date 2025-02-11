# 클래스나 변수 등을 포함한 모듈
# 모듈은 클래스나 변수 등을 포함가능하다.

# mod2 는 원의 지름을 구하는 클래스와 PI의 변수로 이루어져있다. 
import mod2
print(mod2.PI) # mod2 모듈의 PI 변수 사용

# mod2 모듈의 Math 클래스
a = mod2.Math() # a 객체(인스턴스)에 Math 클래스 대입
print(a.solv(2)) # 메서드 solv 사용(원의 지름 구하기)

# mod2 안의 add 함수 사용
print(mod2.add(mod2.PI, 4.4)) # mod2 의 PI변수와 4.4 더하기
