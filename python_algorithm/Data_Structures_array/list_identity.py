# 리스트, 튜플의 동일성 판단

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(list1 is list2) # 두 리스트의 주소가 다름
print(list1[0] is list2[0]) #객체 1과 1은 같은 인터닝 주소

# 리스트 스캔
# 모든 원소 스캔
# 2C-1 (len()함수로 원소 수 미리 파악)
x = ['John', 'George', 'Paul', 'Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

print()
# 2C-2 (enumerate()함수로 모든 원소 스캔)
x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f"x[{i}] = {name}")

print()
# enumerate() 함수 - 인덱스와 원소를 짝지어 튜플로 반환
# enumerate(이터러블, [시작 인덱스])
# 2C-3 (enumerate() 시작 인덱스 지정) (튜플로 나타내줌)
x = ['John', 'George', 'Paul', 'Ringo']

for i2, name2 in enumerate(x, 1): # start = 1
    print(f"x[{i2}] = {name2}")

print()
# 2C-4 (리스트 모든 원소를 스캔 (인덱스 값 사용 X))
x = ['John', 'George', 'Paul', 'Ringo']

for i in x:
    print(i)

# 튜플의 스캔
x = ('John', 'George', 'Paul', 'Ringo')

