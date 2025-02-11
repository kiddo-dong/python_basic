# 1 - 12 까지 8을 건너뜀 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i,end = " ")

# 2
for i in list(range(1,8))+list(range(9,13)):
    print(i,end = ' ')
