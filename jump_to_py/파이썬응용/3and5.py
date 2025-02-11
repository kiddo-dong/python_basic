# 3과 5의 배수 더하기

def sum() :
    num = int(input("1부터 입력한 수까지 3과 5의 배수 더하기 : "))
    three = 0
    five = 0
    for i in range(1,num+1):
        if 0 == i % 3:
            three += i
        elif 0 == i % 5:
            five += i
        else: pass
    return print(three+five)

sum()