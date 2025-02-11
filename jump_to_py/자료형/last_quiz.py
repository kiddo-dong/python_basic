# 되새김 문제

# 1. 평균 점수 구하기
print(f'{"평균 점수":=^30}\n')
name = "홍길동" # input("Enter Name : ")
dic_ = {'국어': 80, '영어': 75, '수학': 55}
dic_li = list(dic_.values())
sum = 0
for i in dic_li:
    sum += i
dic_avg = sum / len(dic_li)
print(f"{name}의 평균 점수 : {dic_avg}")

# 2. 홀수, 짝수 판별하기
print(f"\n{'홀수 짝수 구하기':=^30}\n")
num = 13 # input("정수를 입력하세요 : ")
if int(num) or num.isdigit() :
    num = int(num)
    if 0 == num % 2:
        print("짝수 입니다.")
    else :
        print("홀수 입니다.")
else :
    print("홀수 또는 짝수가 아닙니다.")

# 3. 주민등록번호 나누기
print(f"\n{'주민등록번호':=^30}\n")
citizen_num = '123456-1234567' # input("주민등록번호를 입력하세요(- 포함) : ")
if 14 == len(citizen_num) and citizen_num[6] == '-' : 
    year = citizen_num[:6]
    ci_num = citizen_num[7:]
    print(f"생년원일 : {year}")
    print(f"주민번호 : {ci_num}")
else : 
    print("주민등록번호를 잘못 입력하셨습니다.")

# 4. 주민등록번호 성별
print(f'\n{"성별":=^30}\n')
citiz_num = '123456-1234567' # input("주민등록번호를 입력하세요(-포함) : ")
if 14 == len(citiz_num) and citiz_num[6] == '-' :
    if '1' == citiz_num[7] or '3' == citiz_num[7] :
        print("남성입니다.")
    elif '2' == citiz_num[7] or '4' == citiz_num[7] : 
        print("여성입니다.")
    else :
        print("주민등록번호를 잘못 입력하셨습니다.")
else :
    print("주민등록번호를 잘못 입력하셨습니다.")

# 5. 문자열 바꾸기
print(f'\n{"문자열바꾸기":=^30}\n')
a = 'a:b:c:d'
b = a.replace(':','#')
print(b)

# 6. 리스트 역순 정렬
print(f'\n{"리스트 역순":=^30}\n')
li_sort = [1,3,5,4,2]
li_sort.sort()
li_sort.reverse
print(li_sort)

# 7. 리스트를 문자열로 만들기
print(f'\n{"리스트를 문자열로":=^30}\n')
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 8. 튜플 더하기
print(f'\n{"튜플 더하기":=^30}\n')
a_tu = (1,2,3)
b_tu = (4,)
tu_sum = a_tu + b_tu
print(tu_sum)

# 10. 딕셔너리 값 추출하기
print(f'\n{"값 추출":=^30}\n')
dic = {'A':90, 'B':80, 'C':70}
result_dic = dic.pop('B')
print(dic)
print(result_dic)

# 11. 리스트 중복 제거
print(f'\n{"리스트 중복 제거":=^30}\n')
a_du = [1,1,1,2,2,2,2,3,3,3,4,4,5]
a_set = set(a_du)
b = list(a_set)
print(b)

# 12. 파이썬 변수
a = b = [1,2,3]
a[1] = 4
print(b)
# 결과 : [1,4,3] 이유 : 참조하는 리스트 주소가 같아서


