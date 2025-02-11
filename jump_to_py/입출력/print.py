# print()
# print문의 다양한 표현 방법

# print()
a_num = 123
print(a_num)

a_str = "python"
print(a_str)

a_list = [1, 2, 3]
print(a_list)

# 따음표와 +
# 동일하게 작동한다.
print("py" "thon" "is fun")
print("py" + "thon" + "is fun")

# 문자열 띄어쓰기
# 문자열의 띄어쓰기는 ,를 사용한다.

print("py", "thon", "is fun")

# 한줄에 결과값 출력
# end 를 사용하면 줄바꿈이 아닌 한줄 출력 가능
# end = 끝문자 지정
for i in range(10):
    print(i,end=" | ")

