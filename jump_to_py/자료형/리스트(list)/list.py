# 리스트 자료형
# 숫자의 모음을 숫자나 문자열로 표현하기 위한 자료형
# 리스트 명 = [요소1, 요소2, 요소3, ...]

# 리스트
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, "Life", "is"]
e = [1, 2, ['Life', 'is']]

print(f"\n{'리스트 인덱싱':=^30}\n")


# 리스트 인덱싱(인덱스), 슬라이싱
list_index = [1, 2, 3, 4]
            # 0  1  2  3
print(list_index[3]) # 인덱스 3번의 값인 4를 출력
print(list_index[0] + list_index[1]) # 리스트의 요소 값끼리 수식이 가능하다.
print(list_index[-1]) # 리스트 인덱싱 -1은 뒤에서 부터 첫째자리를 의미.

# 중첩 리스트
# 리스트 안에 리스트를 넣어 중첩된 리스트를 만들 수 있다.
li_dupli = [1, 2, 3, ['a', 'b', 'c']]
print(li_dupli[3]) # 인덱스 3번의 값 출력
print(li_dupli[-1]) # 뒤에서 첫번째 요소 값인 ['a', 'b', 'c'] 출력
print(li_dupli[-1][0]) # 뒤에서 첫번째 요소 값인 중첩 리스트 ['a', 'b', 'c'] 에서 인덱스 0번 출력

li_dupli_th = [1, 2, ['a', 'b', ['Life', 'is']]] #삼중 리스트
print(li_dupli_th[2][2][0]) # Life 출력

print(f"\n{'리스트 슬라이싱':=^30}\n")

# 리스트 슬라이싱
# 문자열과 마찬가지로 리스트에서도 슬라이싱을 적용 할 수 있다.
li_slice = [1, 2, 3, 4, 5, 6, 7]
print(li_slice[0:2]) # 인덱스 0번 부터 인덱스 2번 전까지 출력 
                     # 출력 시 문자열과 다르게 요소 값 각각 출력된다.
print(li_slice[:3]) # 처음 부터 인덱스[2]까지
print(li_slice[3:]) # 인덱스 [3]부터 끝 까지
print(li_slice[:])
# ex) 리스트 [2, 3] 출력
print(li_slice[1:3])

# 중첩 리스트 슬라이싱
li_sl_dupli = [1, 2, 3, ['a', 'b', 'c',], 4, 5]
print(li_sl_dupli[2:5])
print(li_sl_dupli[3][:2])

print(f'\n{"리스트 연산":=^30}\n')

# 리스트 연산
li_a = [1, 2, 3]
li_b = [4, 5, 6]

# 리스트 더하기 
print(li_a + li_b) # 리스트 li_a 와 li_b를 합쳐 [1,2,3,4,5,6] 이 됨.

# 리스트 반복하기
print(li_a * 3) #li_a 에 3을 곱해 3번 출력됨.

# 리스트 길이 구하기 len()함수
ls_length = [1,2,3]
print(len(ls_length))
ls_length_du =[1, 2, 3, ['a', 'b', 'c']] # 4개의 인덱스에 값이 들어있으므로 4출력
print(len(ls_length_du))

# ex) 
a = [1, 2, 3]
print(str(a[1]) + "hi") # a[1] + "hi" 는 type에러 
                        # 정수형 a[1]을 str() 함수를 사용해 문자열로 변환
print(f"\n{'리스트 수정 및 삭제':=^40}\n")

# 리스트의 수정 및 삭제
# 리스트의 요소 값을 수정하거나 삭제 할 수 있다.

# 리스트 값 수정
list_a = [1, 2, 3]
list_a[2] = 4 # 인덱스 2번의 값 3을 4로 변경
print(list_a)

# 리스트 요소 삭제 (del 함수)
list_b = [1, 2, 3]
del list_b[0] # del 함수로 list_b[0]번 삭제
print(list_b) # 삭제되면 인덱스 번호도 당겨짐

list_c = [1, 2, 3, 4, 5]
del list_c[2:] # del 함수에 슬라이싱 적용. 인덱스 2번 부터 끝까지 삭제
print(list_c)
