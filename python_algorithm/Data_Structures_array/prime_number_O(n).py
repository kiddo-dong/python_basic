# 시간 복잡도 O(n)를 고려한 소수 판단 1
# 짝수 배제

count = 0
ptr =  0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        count += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1
        
for i in range(ptr):
    print(prime[i])

print(f"나눗셈을 실행한 횟수 : {count}")