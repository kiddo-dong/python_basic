# 문자열 관련 함수들
# 함수를 사용하려면 변수명 뒤에 . 을 붙인 후 함수명 사용
# 변수명.함수()

# count() 함수 (지정 문자 개수 세기)
str = "hobby"
print(str.count('b'))

# find() 함수 (지정 문자 인덱스 반환)
str = "Python is the best choice"
print(str.find('b'))
print(str.find('k')) # 문자열에 존재하지않는 문자면 -1 반환

# index() 함수 (지정 문자 인덱스 반환)
str = "Life is too short"
print(str.index('t'))
# print(str.index('k')) # 존재하지않는 문자면 find()함수와 다르게 에러 발생

# join() 함수 (문자 하나마다 문자열 삽입)
str = "abcdef"
print(",".join(str))

# upper() 함수 (소문자 대문자로 변환)
str = "hello"
print(str.upper())

# lower() 함수 (대문자 소문자로 변환)
str = "HELLO"
print(str.lower())

# lstrip(), rstrip() 함수 (가장 왼쪽, 오른쪽 공백 삭제)
str = "  hi  "
print(str.lstrip()) #왼쪽
print(str.rstrip()) #오른쪽

# replace() 함수 (문자열 변경)
str = "Hello donghyun"
print(str.replace("donghyun","World!"))

# split() 함수 (문자열 나누기)
str = "abcd : efgh"
print(str.split()) # 공백 기준
print(str.split(":")) # 지정한 문자나 문자열 기준

