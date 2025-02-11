# 문자열 포매팅
# 문자열 안에 어떤 값을 삽입하는 방법

'''
문자열 포맷 코드
%s 문자열(string)
%c 문자 하나(char)
%d 정수 (integer, decimal)
%f 부동소수 (float)
%o 8진수
%x 16진수
%%  Literal (문자 % 자체)
'''
print("I eat %d apple" %3) # 정수형 숫자 포매팅
print("Pi : %f" %3.141592) # 실수형 숫자 포매팅
print("I eat %s apple" %"five") # 문자열 포매팅

number = 5
print("number : %d" %number) # 변수를 포매팅 (정수형)
print("string : %s" %number) # 변수인 5가 문자열로 변환 되면 포매팅
str_format = "three"
print("number : %d string : %s" %(number, str_format)) # 2개 이상 포매팅
print("per : %d%%" %number) # 포매팅과 %를 같이 사용할땐 %%
pi = 3.1415929835
flo = 12345.2323
print("pi : %0.2f" %pi) # 소수점 둘째 자리까지 포매팅
print("flo : %3.2f"%flo)
