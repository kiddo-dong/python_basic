# 홀짝 판별
def is_odd(number):
    if 0 != number % 2:
        return "홀수"
    else:
        return "짝수"
# init = int(input())
print(is_odd(3))

# 모든 입력의 평균값 출력
def all_avg(*in_put):
    all_result  = 0
    for all_i in in_put:
        all_result += all_i
    return all_result / len(in_put)
print(all_avg(1,2,3,4,5,6,7))
print(all_avg(3,6,9,12,15))

# 프로그램 오류 수정하기
'''
num1 = input("숫자 입력 : ")
num2 = input("슷자 입력 : ")
#수정부분
new_num1 = int(num1)
new_num2 = int(num2)
total =  new_num1 + new_num2
print(total)
'''
# 오류 수정2
f1 = open("test.txt",'w')
f1.write("Life is ")
f1.close()
f2 = open("test.txt",'r')
print(f2.read())
f2.close()

'''
# 사용자 입력을 txt 파일로 저장하기
user_input = input("저장할 내용을 입력하세요 : ")
user_file = 
user_file.write(user_input)
user_file.write('\n')
print("저장되었습니다.")
user_file.close()
'''

# 파일의 문자열 변경
file_change = open('D:\\jump_to_py\\입출력\\user_file.txt','r')
change = file_change.read()
file_change.close()
change = change.replace('java', 'python')

file_new = open('D:\\jump_to_py\\입출력\\user_file.txt','w')
file_new.write(change)
file_change.close()
