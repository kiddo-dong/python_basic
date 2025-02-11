# 원하는 구구단을 입력받아 출력
def gugu():
    num = int(input("원하는 구구단 출력 (2~9 입력)"))
    for i in range(2,10):
        print(f"{num} x {i} = {num * i}")
    

gugu()