# 2. while문 1 - 1000 3의 배수 합 구하기
num = 0
sum = 0
while num < 1001:
    num += 1
    if 0 == num % 3:
        sum += num
    else:
        pass
print(f"3의 배수의 합은 {sum}")

print(f"\n{'별 표시':=^30}\n")
#별 표시하기
star = 1
while star <= 5:
    print(star * "*")
    star += 1

print(f"\n{'1부터 100 출력':=^30}\n")
# 1부터 100까지 출력
for i in range(1,101):
    print(i)


print(f"\n{'평균점수 구하기':=^30}\n")
# 평균점수 구하기
A_cl =[70,60,55,75,95,90,80,80,85,100]
sum = 0
for i in A_cl:
    sum += i
avg = sum / len(A_cl)
print(f'A반 학생의 평균 점수 : {avg}')


print(f"\n{'리스트 컴프리헨션':=^30}\n")
# 리스트 컴프리헨션
numbers = [1, 2 ,3, 4, 5]
result = [n * 2 for n in numbers if n % 2 ==1]
print(result)






