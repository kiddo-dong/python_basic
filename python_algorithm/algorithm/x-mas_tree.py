# 트리를 만들어보자
a=int(input("나뭇 잎 길이 :"))
b=int(input("나무 잎 수 : "))
c=int(input("줄기 갯수 : "))
for _ in range(b):
    for i in range(a):
        for _ in range(a - i - 1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        print()
for _ in range(c):
    print(" "*((j+1)//2),end="")
    print("*")