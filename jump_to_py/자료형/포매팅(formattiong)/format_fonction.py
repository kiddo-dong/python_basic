# format 함수를 사용한 포매팅
# 이전 formatting보다 발전된 스타일

print("number : {0}".format(3)) # 중괄호 format에 3 대입
print("string : {0}".format("five")) # 문자열 "five" 대입
num = 6
print("number : {0}".format(num)) # 변수 대입

num = 1
str = "seven" # 2개 이상의 값 넣기
print("number : {0} string : {1}".format(num,str)) # {0} 에는 num {1}에는 str대입 {0},{1}은 format의 인덱스


print("number : {num1} string : {str1}".format(num1 = 10, str1 = "nine")) # format 함수에 변수 정의
                                                                          # format 함수 안에서 변수를 선언 시 문자열 {}에서 변수명 기입

# formatting 정렬
"""
formatting 정렬은 오른쪽, 왼쪽, 가운데가 있음
화살표 방향으로 생각
:> 오른쪽 정렬
:< 왼쪽 정렬
:^ 가운데 정렬
"""
print("number : {0} string : {str2}".format(8,str2 = "hello")) # 인덱스와 변수 정의 혼용
print("sort : {0:<}".format("hi")) # 왼쪽으로 정렬
print("sort : {0:<10}".format("hi")) #왼쪽으로 정렬, 문자열 총 10자리
print("sort : {0:>}".format("hi")) # 오른쪽으로 정렬
print("sort : {0:>10}".format("hi")) # 오른쪽으로 정렬, 문자열 총 10자리
print("sort : {0:^10}".format("hi")) # 가운데 정렬, 문자열 총 10자리
print("sort : {0:=^10}".format("hi")) # 가운데 정렬, 문자열 총 10자리, 공백은 =으로 채우기
print("sort : {0:@>10}".format("hi")) # 오른쪽 정렬, 문자열 총 10자리, 공백은 @으로 채우기

flo = 3.12345678
print("float : {0:0.2f}".format(flo)) # flo를 소수점 두자리까지 출력
print("float : {0:>10.2f}".format(flo)) # flo를 소수점 두자리까지 출력, 오른쪽으로 정렬 및 문자열 총 10자리
print("{{cjdkd}}".format()) # {}를 포매팅이 아닌 문자 그대로 사용