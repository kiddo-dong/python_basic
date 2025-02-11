# 10진수 정숫값을 입력받아 2 ~ 36 진수 변환

# 진수 변환
def card_conv(x:int, r:int) -> str:
    d = ''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x > 0:
        d = d + dchar[x % r]
        x = x // r
    
    return d[::-1]


# 함수 호출 및 사용
if __name__ == "__main__":
    while True:
        while True:
            print('10진수 -> n진수 변환기')
            no = int(input("음수가 아닌 정수를 입력 : "))
            if no > 0 :
                break
    
        while True:
            cd = int(input("변환을 원하는 진수 입력 (2~36)"))
            if 2 <= cd <= 36 : 
                break
        
        print(f"{cd}진수로 변환 : {card_conv(no, cd)}")

        retry = input("한번 더 변환 할까요? ('Y' 예, 'N' 아니요)")
        if retry in {'N', 'n'}:
            break