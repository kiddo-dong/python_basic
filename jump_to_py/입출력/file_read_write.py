# 파일 읽고 쓰기
# 파일의 입출력 방법

# 파일 생성하기

# open() 함수
# 파일_객체명 = open(파일 이름, 파일 열기 모드)
new_file = open('새파일.txt','w')
new_file.close()

# 파일 열기모드
# r - 읽기 모드 : 읽기만 가능
# w - 쓰기 모드 : 쓰기 가능
# a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 떄 사용 

# 경로 지정
load_file = open("D:\\jump_to_py\\입출력\\경로.txt",'w')
load_file.close()


# write() 함수
# write()는 print문처럼 사용 가능
# 파일을 쓰기모드로 열어 내용 쓰기

# write() 안에 직접 쓰기
write_file = open('D:\\jump_to_py\\입출력\\써보기.txt','w')
write_file.write("안녕하세요")
write_file.close()

# write() 에 변수 넣기
write_val = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','w')
for i in range(1,10):
    write_val.write(f"{i}번째 줄입니다.\n")
write_val.close()


# 파일을 읽는 여러가지 방법

# readline() 함수
# 가장 첫번쨰 줄 출력
read_line = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','r')
line = read_line.readline()
print(line)
read_line.close()
# 모든 줄 출력
read_line = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','r')
while True:
    line = read_line.readline()
    if not line: break
    print(line)
read_line.close()

# readlines() 함수
#모든줄을 읽어 줄단위로 리턴
file_lines = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','r')
lines = file_lines.readlines()
for j in lines:
    print(j)
file_lines.close()

# read() 함수
# 전체 내용 리턴
read_line = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','r')
data = read_line.read()
print(data)
read_line.close()

# 파일 객체를 for문과 함께 사용
# 줄단위로 출력
for_line = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','r')
for i in for_line:
    print(i)
for_line.close()


# 파일에 새 내용 추가
# a - 추가모드 사용
add_line = open('D:\\jump_to_py\\입출력\\반복출력ex.txt','a')
for u in range(11,20):
    add_line.write(f'{u}번째 줄입니다.\n')
add_line.close()

# with문과 함께 사용하기
# open()과 close()를 자동처리
# with open(파일명, 모드) as 파일_객체명 :
with open('D:\\jump_to_py\\입출력\\with.txt','w') as with_test:
    with_test.write("오 이게 되네")