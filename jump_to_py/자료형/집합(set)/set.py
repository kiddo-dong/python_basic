# 집합 자료형
# 집합 처리에 관한 자료형
# 중복허용 x, 순서 x
# 집합명 = set()

# 집합 자료형 
s1 = set([1, 2, 3]) # 수 집합
print(s1)

s2 = set('hello') # 문자열 집합
print(s2)


# 집합 인덱싱
# 집합을 인덱싱 하고 싶다면 리스트나, 튜플로 변환 해야한다.
s3 = set([1, 2, 3]) 
l1 = list(s3) # 집합을 리스트로 변환
print(l1)
print(l1[2])

s4 = set([1, 2, 3])
t1 = tuple(s4) # 집합을 튜플로 변환
print(t1)
print(t1[1])

# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2) # 교집합
print(s1.intersection(s2))

print(s1 | s2) # 합집합
print(s1.union(s2))

print(s1 - s2) # 차집합
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

