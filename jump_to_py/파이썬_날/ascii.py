# 유니코드 
# 세계 표준 문자셋

# 유니코드 문자열 다루기

# 인코딩 - 유니코드 바이트코드로 변환
a = "Life is too short" # 유니코드 문자열
print(type(a))
b = a.encode('utf-8') # 바이트 문자열로 변환
print(b)
print(type(b))

# 한글 유니코드 문자열을 아스키 방식으로 인코딩
a = "한글"
# a.encode('ascii') # 에러 발생
a.encode('euc-kr')
a.encode('utf-8')

# 디코딩 - 바이트 코드 유니코드로 변환
a = '한글'
b = a.encode('euc-kr') # 바이트 코드로 변환
b.decode('euc-kr') # 유니코드로 변환
# 같은 데이터셋 타입으로 디코딩을 해야한다.

with open('euc-kr.txt',encoding = 'euc-kr') as f:
    data = f.read()

data = data + '\n'