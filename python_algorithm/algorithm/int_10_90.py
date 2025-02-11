# 10 부터 99 정수입력

while True:
    num = int(input("수 입력 : "))
    if num >= 10 and num <= 99 :
        break
print(f"입력한 정수는 : {num}")