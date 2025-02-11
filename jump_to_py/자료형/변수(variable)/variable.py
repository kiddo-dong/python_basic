# 변수
# 다른 언어와 다르게 변수의 자료형을 지정하지 않음.
# 변수명 = 변수에_저장할_값
# 변수명의 주소에 값을 저장하는 방식

# 변수 (variable)
a = 1 # 변수 a에 1의 값 저장
b = "python" # 변수 b에 문자열 저장
c = [1, 2, 3] # 변수 c에 리스트 데이터 저장

# id() 함수 (변수의 주소)
adr = [1, 2, 3] # 리스트 변수 adr (객체)
print(id(adr)) # id 함수로 변수 adr의 주소를 출력
print(f"adr[0] = {id(adr[0])} | adr[1] = {id(adr[1])} | adr[2] = {id(adr[2])}") # adr 리스트 안의 각각 값의 주소가 다름
# 즉, adr의 주소 안의 값들이 각각의 주소값을 또 가지고 있음.

# 변수의 복사
# C언어는 절차 지향이므로 변수마다 각각의 주소가 다르지만,
# 파이썬은 객체 지향이므로 변수에 변수를 대입하면 주소 값을 저장하므로 동안한 주소를 가지게 됨.
a = [1, 2, 3]
b = a # 변수 a의 주소를 b에 복사.
print(f"a = {a} | b = {b}\n") # 동일한 주소를 가리켜 같은값이 나옴
print(f"a_id = {id(a)} | b_id = {id(b)}") # id() 함수. 변수 a와 변수 b의 주소가 같다는 것을 알 수있음.
print(a is b) # bool(a == b) 와 동일

a[1] = 4 # 변수 a[1]의 주소가 가리키는 값을 변경, 주소는 그대로
print(f"\n{a}")
print(b) # 변수 b는 변수 a와 같은 리스트의 주소를 가리킴

# 수, 문자열 복사
# 수, 문자열은 복사 시 주소가 아닌 값이 저장됨
test1 = 4
test2 = test1
test1 = 5 
print(id(test1))
print(id(test2))
test1 = 3
print(id(test1))
test1 = 4
print(id(test1))


# 변수를 다른 주소로 복사 ()
# [:]를 이용
a_cp = [1, 2, 3]
b_cp = a_cp[:] # 리스트 a의 리스트 전체 값을 b에 복사.
               # 주소가 아닌 a의 리스트 값을 복사 
a_cp[1] = 4 # 리스트 a_cp의 값 변환
print(f"a_cp = {a_cp}| b_cp = {b_cp}") # 주소가 아닌 리스트의 전체 값을 복사하였기에 주소가 다르다
print(f"a_cp_id = {id(a_cp)} | b_cp_id = {id(b_cp)}") # 주소 확인

from copy import copy # 라이브러리 함수 불러오기
a = [1, 2, 3]
b = copy(a) # copy 함수로 a 리스트 복사
print(b is a)

a_li = [1, 2, 3]
b_li = a_li.copy() # 리스트 내장 함수 copy()
print(a_li is b_li)


# 변수를 만드는 여러가지 방법
a_tu1, b_tu1 = ('python', 'Life') # 튜플
(a_tu2, b_tu2) = 'python', 'Life' # 튜플
a_tu3, b_tu3 = 'python', 'Life' # 튜플
print(a_tu3)

a_a = b_b ='python' # 여러개의 변수에 같은 값 대입
print(f"{a_a} | {b_b}")

# 변수의 값 바꾸기
a_ch = 3
b_ch = 5
a_ch, b_ch = b_ch, a_ch # a는 b의 값으로 b는 a의 값으로 변경
print(f"a = {a_ch} | b = {b_ch}")

# 리스트 주소는 다르지만 리스트 안 각각의 요소들은 같은 주소
a = [1, 2, 3] 
b = [1, 2, 3]
print(a is b)


