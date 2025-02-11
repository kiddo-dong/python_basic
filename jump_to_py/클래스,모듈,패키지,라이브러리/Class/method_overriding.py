# 매서드 오버라이딩
# 매서드 오버라이딩 - 부모클래스에 있는 메소드를 자식 클래스에서 재정의.

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

# 메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):  # 부모 클래스인 FourCal의 동일한 메소드인 def div() 메소드를 재정의 
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

a = SafeFourCal(4, 0) # 객체 a
print(f"객체 a : add값 {a.add()} | sub값 {a.sub()} | mul값 {a.mul()} | div값 {a.div()}")
# FourCal의 a.div()를 재정의하여 자식클래스인 SafeFourCal로 재정의하여 오류를 예외 처리함