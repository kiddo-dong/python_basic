# 별 출력
print(f'\n{"1번":=^30}')
n = 7
for i in range(n):
    for _ in range(i+1):
        print("*",end="")
    print()

print(f'\n{"2번":=^30}')
for i in range(n):
    for _ in range(n-i-1):
        print(" ",end="")
    for _ in range(i+1):
        print('*',end="")
    print()

print(f'\n{"3번":=^30}')
for i in range(n,0,-1):
    for _ in range(i):
        print("*", end='')
    print()

print(f'\n{"4번":=^30}')
for i in range(n):
    for _ in range(n-i-1):
        print(" ",end="")
    for _ in range(2*i+1):
        print("*",end="")
    print()

print(f'\n{"5번":=^30}')
for i in range(n):
    if i == 0 or i==n-1:
        print("*" * n)
    else : print("*" + " " * (n-2) + "*")
