# 모듈
# 함수나 변수 또는 클래스를 모아놓은 파이썬 파일
# 모듈을 사용하기 위해선 모듈을 불러와야한다.

"""
1. 모듈을 불러와 사용
import 모듈_이름
모듈명.모듈함수()

2. 모듈 이름없이 함수를 사용
from 모듈_이름 import 모듈_함수
모듈함수()
"""
# mod1 모듈을 만들고 실행
import mod1 # 모듈 mod1 가져오기

print(mod1.add(1, 2)) # import한 mod1의 함수 add 사용
print(mod1.sub(6, 2)) # import한 mod1의 함수 sub 사용

# mod1 모듈 이름 없이 함수 사용
from mod1 import add # mod1의 add 함수를 가져온다.

print(add(3,5)) # mod1의 add함수를 import 했으므로 모듈명은 안적어도된다.

# , 사용하기 (여러 모듈 함수 import)
from mod1 import add, sub # mod1의 add, sub 함수 가져오기.
print(f",사용 add : {add(1, 3)}")
print(f",사용 sub : {sub(4, 1)}")

# * 사용하기 (모든 표듈 함수 import)
from mod1 import *
print(f"*사용 add : {add(2, 5)}")
print(f"*사용 sub : {sub(9, 3)}")

