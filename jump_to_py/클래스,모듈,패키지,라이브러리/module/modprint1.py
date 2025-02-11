# if __name__ == "__main__": 의 의미
# 이 모듈파일을 실행하면 import한 파일에서 프린트문이 같이 실행 될 것이다.
# if __name__ == "__main__": 을 사용하면 이 파일에서는 True 이지만 이 파일을 import한 파일에서는 false로 작동한다.


def add(a, b):
    return a + b
def sub(a, b):
    return a - b

if __name__ == "__main__" :
    print(add(1, 4))
    print(sub(4 ,2))
