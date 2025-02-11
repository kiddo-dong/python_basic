# 딕셔너리 관련 함수들

# keys() 함수 (dic_keys 리턴, Key 모음)
a = {'name': '최동현', 'phone': '010-6691-6559', 'birth': '020207'}
print(a.keys())
print(list(a.keys())) # dic_keys를 리스트로 변환

for i in a.keys():  # dic_Keys 값 반복문 
    print(i)

# Values() 함수 (dic_Values 리턴, Value 모음)
b = {'name': '최동현', 'phone': '010-6691-6559', 'birth': '020207'}
print(b.values())
print(tuple(b.values())) # dic_Values 튜플로 변환

for i in b.values(): # dic_Values 값 반복문
    print(i)

# items() 함수 (dic_items 리턴, Key와 Values의 쌍을 튜플로 묶은 값)
it = {'name': '최동현', 'phone': '010-6691-6559', 'birth': '020207'}
print(it.items())

for i in it.items(): #dic_items 값 반복문
    print(i)

# clear() 함수 (Key: Value 쌍 모두 지우기)
cl = {1: 'a', 2: 'b'}
a.clear()
print(a)

# get() 함수 (Key로 Value 값 얻기)
g = {'name': '최동현', 'phone': '010-6691-6559', 'birth': '020207'}
print(g.get('phone')) # phone 에 해당하는 value 값 출력
print(g.get('age')) # 딕셔너리에 존재하지 않은 키, 값이 없으므로 None
print(g.get('age', 'not in age')) # age 키가 존재하지 않아 Defualt 값  not in age 출력

# in 함수 (Key 찾기, True or False)
key_in = {'name': '최동현', 'phone': '010-6691-6559', 'birth': '020207'}
print('name' in key_in)
print('age' in key_in)
