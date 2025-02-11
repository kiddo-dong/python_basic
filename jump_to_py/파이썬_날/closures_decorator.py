# 클로저
# 함수 안에 내부 함수 구현 후 그 내부함수를 리턴 하는 함수
'''
def mul3(n):
    return n * 3
def mul5(n):
   return n * 5
'''
# 필요시마다 함수를 만드는 것은 비효율적
# 클로저 예시
def Mul(m):
    def wra(n):
        return m*n
    return wra

if __name__ == "__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))
    print(mul5(10))


#데코레이터

def myfunc():
    print("함수가 실행됨")

