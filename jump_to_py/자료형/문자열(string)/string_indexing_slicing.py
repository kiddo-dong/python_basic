# 문자열 인덱싱(인덱스)과 슬라이싱
# 인덱싱(인덱스)은 가리키는 것, 슬라이싱은 잘라내는 것

#문자열 인덱싱(인덱스)
str = "Life is too short, You need Python" # str이라는 문자열
     # 0                                33 # 인덱스 번호 L은 0, n은 33이다. 즉, 인덱스 번호는 0부터 시작하며 문자 하나하나에 인덱스 번호가 있다.
print(str[3]) # str 문자열 변수의 인덱스 번호 3번에 해당하는 e 출력.
print(str[12]) # 12번 인덱스 s 출력
print()

# 문자열 인덱스 응용
print(str[0]) # L
print(str[30]) # t]
print(str[-1]) # n 문자열 인덱스 앞에 -의 의미는 뒤에서 부터 수를 센다.
print(str[-0]) # -0은 0이므로 L 출력
print(str[11 + 1]) # 11번째 인덱스인 공백에 1을 더하면 12번째 인덱스의 s 출력.
print(str[14 - 1]) # 14 - 1은 13이므로 인덱스 13인 h 출력.
print(str[-10 + 2]) # -10 + 1은 -8이므로 뒤에서부터 8번째자리인 d 출력.

print("=" * 50)
#===========================================================================================================================================================================================

# 문자열 슬라이싱
# 내가 원하는 문자나 단어를 뽑아냄.
str = "Life is too short, You need Python"
     # 0                                33
str_find = str[0] + str[1] + str[2] + str[3] # 문자 하나하나를 연결하여 원하는 단어 Life를 출력
print(str_find) # 시간과 효율이 좋지않음
print(str[0:4]) # 인덱스 0번부터 인덱스 4번 전까지 출력
                # 0 <= str < 4 까지라는 말이다. 즉, str[0 ~ 3] 까지 출력
                # Life 가 출력됨.
print(str[0:3]) # Lif 출력. 인덱스 0부터 2까지[0,1,2]
print(str[5:7]) # is 출력
print()

print("=" * 10 +"문자열 슬라이싱 응용" + "=" * 10)
# 문자열 슬라이싱 응용
str = "Life is too short, You need Python"
     # 0                                33

print(str[8:11]) # 8번 인덱스인 t부터 11번 전 o까지 출력.
                 # too 출력

print(str[-11:27]) # n은 뒤에서 부터 11번째 자리에 있으므로 -11
                   # d의 인덱스는 26
                   # 뒤에서부터 11번째 자리부터 27번 전까지 출력.
                   # need 출력.

print(str[19:-7]) # 인덱스 19번인 Y부터 끝에서 일곱번째 전인 d 까지 출력.
                  # Yoo need 출력.

print(str[19:]) # 문자열 끝번호 생략
                # 인덱스 번호 19인 Y부터 문자열 끝까지 출력.
                # You need Python 출력.

print(str[:17]) # 문자열 첫 번호 생략
                # 문자열 처음부터 인덱스 번호 17 전까지 출력.
                # Life is too short 출력.

print(str[:]) # 시작 번호와 끝 번호 생략 
              # 문자열 처음부터 끝까지 출력.

# 슬라이싱으로 문자열 나누기
# 자주 사용하는 슬라이싱 기법
str_sli = "20230331Rainy" # 문자열을 날짜와 날씨로 슬라이싱
date = str_sli[:8]
weather = str_sli[8:]
print(date)
print(weather)

# 년도, 월일, 날씨로 슬라이싱
year = str_sli[:4]
date = str_sli[4:8]
weather =  str_sli[8:]
print(year)
print(date)
print(weather)

# 문자열 문자 변경
'''
에러가 나는 코드
str_change = "pithon" # pithon의 i를 y로 변경
str_change[1] = "y" # pithon의 인덱스 1번의 값을 y로 변경
print(str_change)
'''

# 위의 코드 처럼 문자열은 변경이 불가능하다. 에러가 남
# 슬라이싱을 이용하여 문자열 변경하는 방법
str_change = "pithon"
str_new = str_change[:1] + 'y' + str_change[2:] # 문자열 pithon 에서 인덱스 0번 까지 출력하여 인덱스 0번까지 저장. 
                                                # 1번 인덱스인 i 대신 y를 더 해 첨가한 후 인덱스 2번부터 문자열 끝까지 str_new변수에 저장
print(str_new)                                  # python 출력.
