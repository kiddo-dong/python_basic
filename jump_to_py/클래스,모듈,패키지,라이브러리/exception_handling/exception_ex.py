# 오류 회피하기
# pass 사용
try:
    f = open("나없는파일",'r')
except FileNotFoundError:
    pass
 # FileNotFoundError 발생 시 pass로 오류를 회피


# 오류 일부러 발생 시키기
# 오류를 일부러 발생시켜야 하는 경우 사용한다.

# raise 사용
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

class dragonfly(Bird):
    pass

eagle = Eagle()
eagle.fly()

Dfly = dragonfly()
dragonfly.fly() # raise NotImplementedError 발생한다.

