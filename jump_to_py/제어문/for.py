# for
# 반복문
# 가장 직관적이다.
"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행문장1
    수행문장2...
"""
# for 문
test_list = ['one', 'two', 'three']
for i in test_list: # test_list를 i에 대입
    print(i)

# 다양한 for문 사용
# 튜플
list_for = (1,2,3), (4,5,6)
for (on, tw, th) in list_for:
    print(on, tw, th)

# 리스트 안의 튜플
list_tu_for = [(1, 2), (3, 4), (5, 6)]
for (a, b) in list_tu_for:
    print(list_tu_for[2])

# for문 응용
# 리스트 이용
marks = [90, 25, 67, 45, 80]
count = 0

for i in marks:
    count += 1
    if i >= 60:
        print(f"{count}번째 학생은 합격입니다.")
    else :
        print(f"{count}번째 학생은 불합격입니다,")

# 불합격 continue 합격만 출력
marks_co = [90, 25, 67, 45, 80]
count_co = 0

for i in marks_co:
    count_co += 1
    if i < 60:
        continue
    print(f"{count_co}번 학생 축하합니다. 합격입니다.")


# range() 함수 (범위 지정하여 반복, 증감)
a = range(10) # 0 부터 10미만
print(a)

b = range(1,11) # 1부터 11미만
print(b)

c = range(10, 0) # 10부터 1까지
print(c)

print(f'{"range 예시":=^30}')
# 1부터 10 까지 더하기
result = 0
for i in range(1,11):
    result = result + i
print(result)

# 10부터 1까지 뺴기
result = 0
for j in range(10,0):
    result = result - j
print(result)

# ex) 
print(f"\n{'ex점수':=^30}\n")

marks = [90, 25, 67, 45, 80] # 리스트
for number in range(len(marks)): # marks의 길이인 5 range, range 0부터 5미만을 number에 대입
    if marks[number] < 60 : # marks의 요소값을 0부터 4까지 증가하면서 반복, 요소값이 60보다 작으면 실행
        continue
    print(f"{number+1}번째 학생은 합격입니다.")

print(f'\n{"1~100의 합":=^30}\n')
# 1 부터 100까지의 합
sum = 0
for i in range(1,101):
    sum += i
print(sum)

# 구구단 출력
for i in range(2,10):
    print()
    for j in range(2,10):
        print(f"{i} x {j} = {i*j}",end = " ")

print(f'\n{"리스트 컴프리헨션":=^30}\n')
# 리스트 컴프리헨션
# 코드의 간결화
'''
[표현식 for 항목 in 반복가능개체 if 조건명] # if는 생략가능
'''


a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)