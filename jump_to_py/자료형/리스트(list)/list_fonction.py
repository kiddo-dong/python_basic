# 리스트 관련 함수
# 리스트명.함수명()

# append() 함수 (맨 끝에 요소 추가)
app = [1, 2, 3]
app.append(4) # 리스트 맨 마지막에 4 추가
print(app)

app_du = [1, 2, 3]
app_du.append([4,5]) # 리스트 맨 마지막에 [4,5] 추가
print(app_du) # 중첩 리스트

# sort() 함수 (리스트 정렬)
sort_a = [1, 3, 4, 2]
sort_a.sort() # 정렬
              # 내림차순 .sort(reverse=True)
print(sort_a)

sort_b = ['b', 'a', 'd', 'c']
sort_b.sort()
print(sort_b) # 알파벳 정렬

# reverse() 함수 (리스트 역순)
rever_a = ['b', 'a', 'd', 'c']
rever_a.reverse() # 리스트 역순
print(rever_a)

# index() 함수 (인덱스 위치)
index_a = [1, 2, 3, 6, 5, 8]
print(index_a.index(6))

# insert() 함수 (요소 삽입)
insert_a = [1, 2, 3, 5, 6]
insert_a.insert(3, 4) # 인덱스 3번에 값 4입력
print(insert_a)

# remove() 함수 (지정 요소 삭제)
remove_a = [1, 2, 3, 4]
remove_a.remove(4)
print(remove_a)

# pop() 함수 (인덱스 번호 요소 리턴 후 삭제)
pop_a = [1, 2, 3, 4]
pop_a.pop(2) # 생략 시 맨 끝 리턴 후 삭제
print(pop_a)

# count() 함수 (지정 숫자, 문자 개수 세기)
count_a = [1, 2, 3, 1]
print(count_a.count(1))

# extend() 함수 (리스트 확장)
extend_a = [1, 2]
extend_a.extend([3, 4]) #리스트에 3, 4를 추가 확장
print(extend_a)

