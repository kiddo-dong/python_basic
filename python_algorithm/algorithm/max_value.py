# 알고리즘 기초
# 세 정수의 최댓값 구하기
print("세 정수의 최댓값을 구하세요.")
a = input("정수 입력 : ")
b = input("정수 입력 : ")
c = input("정수 입력 : ")

# 순차 구조 - 한문장씩 처리되는 구조
maximum = a
if b > maximum : maximum = b
if c > maximum : maximum = c
print(f"최댓값은 {maximum}입니다.")
# 선택 구조 - 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경 되는 것