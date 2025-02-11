# 상속
# 상속 - 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것.
# 상속을 받은 클래스는 상속을 한 클래스의 모든 기능을 사용 할 수 있다.
# 기존의 클래스는 그대로 놔두고 클래스의 기능을 확장할 때 주로 사용한다.

# class 클래스_명(상속할_클래스명)

# 사칙연산 class 상속받기
class FourCal :
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

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

class MoreFourCalculator(FourCal):
    def pow(self): 
        result = self.first ** self.second
        return result
# FourCal클래스의 기능들을 상속받은 MoreFourCalculator클래스에서 pow함수 확장

a = FourCal(4, 2) # 객체 a
b = FourCal(3, 8) # 객체 b

print(f"객체 a : add값 {a.add()} | sub값 {a.sub()} | mul값 {a.mul()} | div값 {a.div()}")
print(f"객체 b : add값 {b.add()} | sub값 {b.sub()} | mul값 {b.mul()} | div값 {b.div()}")
# pow값 {b.pow()} - FourCal클래스는 pow()함수가 정의되어있지 않으므로 사용이 어렵다.


# 객체 a,b를 새 클래스에 대입시 현클래스와 연결이 끊기고 다시 대입한 새 클래스에 연결됨.
a = MoreFourCalculator(4, 2) # 객체 a
b = MoreFourCalculator(3, 8) # 객체 b
print(f"객체 a : add값 {a.add()} | sub값 {a.sub()} | mul값 {a.mul()} | div값 {a.div()} | pow값 {a.pow()}")
print(f"객체 b : add값 {b.add()} | sub값 {b.sub()} | mul값 {b.mul()} | div값 {b.div()} | pow값 {b.pow()}")
# MoreFourCalculator클래스에서 확장한 pow()함수를 사용할 수있다.


