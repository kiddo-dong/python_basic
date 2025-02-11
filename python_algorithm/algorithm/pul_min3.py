# +- 번갈아 가며 출력
# 최적화 코드

n = int(input("+,- 번갈아 출력"))
for _ in range(n // 2):
    print("+-",end = "")
if n % 2:
    print("+",end="")