area = int(input("넓이 입력"))
# 32
for i in range(1, area + 1):
    if i * i > area: break
    if area % i : continue
    print(f'{i} x {area//i}')