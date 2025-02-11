# 내장 함수
# print(f"\n{'':=^30}")

# abs() 함수 (절댓값 리턴)
print(f"\n{'abs()':=^30}")
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all() 함수 (반복가능 데이터 True, False 확인,(and))
# 데이터가 하나라도 False이면 False 출력
print(f"\n{'all()':=^30}")
li_a = [1, 2, 3]
li_b = [1, 2, 3, 0]

print(all(li_a))
print(all(li_b)) # 0이 리스트에 존재함으로 false 출력

# any() 함수 (반복가능 데이터 True, False 확인,(or))
# 데이터가 하나라도 True이면 True 출력
print(f"\n{'any()':=^30}")
li_a = [1, 2, 3]
li_b = [1, 2, 3, 0]

print(any(li_a))
print(any(li_b))

# chr() 함수 (유니코드 변환)
print(f"\n{'chr()':=^30}")

print(chr(97))
print(chr(44032))
print(chr(65))

# dir() 함수 (객체가 지닌 변수나 함수 출력)
print(f"\n{'dir()':=^30}")

print(dir([1,2,3]))
print(dir({'1' : 'a', '2' : 'b'}))

# divmod(x, y) 함수 (x를 y로 나눈 몫과 나머지 튜플로 리턴)
print(f"\n{'divmod()':=^30}")
print(divmod(7,3))

# enumerate() 함수 (순서가있는 데이터를 인덱스와 값을 포함해 리턴)
print(f"\n{'enumerate()':=^30}")
for i, name in enumerate(["body", "foo","bar"]):
    print(i, name)


# eval() 함수 (문자열로 구성된 식을 입력으로 받아 결과값 리턴)
print(f"\n{'eval()':=^30}")
print(eval("1+2"))
print(eval('"hi" + "a"'))

# filter(함수, 반복가능데이터) 함수 (리턴값이 참인것만 묶어서 리턴)
print(f"\n{'filter()':=^30}")
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))


# hex() 함수 (16진수 문자열로 변환)
print(f"\n{'hex()':=^30}")

print(hex(234))
print(hex(3))


# id() 함수 (객체의 고유 주솟값 리턴)
print(f"\n{'id()':=^30}")
id_a = 3

print(id(3))
print(id(id_a))    # 3이라는 객체의 고유 주솟값



# input() 함수 (사용자의 입력을 받음)
print(f"\n{'input()':=^30}")
# a = input("프롬프트입니다 : ")

# int() 함수 (문자열 형태의 숫자, 소수점이 있는 숫자를 정수로 리턴)
print(f"\n{'int()':=^30}")
print(int('3'))
print(int(3.4))

# isinstance(객체, 클래스) 함수 (객체가 클래스의 인스턴스인지 판단, True, False)
print(f"\n{'isinstance()':=^30}")
class Person: pass

cla_a = Person()
print(isinstance(cla_a, Person))

# len() 함수 (길이를 리턴)
print(f"\n{'len()':=^30}")
print(len("python"))
print(len([1, 2, 3]))
print(len((1, 'a')))

# list() 함수 (반복 가능 데이터를 리스트로 리턴)
print(f"\n{'list()':=^30}")
print(list("python"))
print(list((1, 2, 3)))

# map(함수, 반복 가능 데이터) 함수 (구문 간결 함수)
print(f"\n{'map()':=^30}")
def two_times(x):
    return x * 2
print(list(map(two_times, [1, 2, 3, 4])))

# max(), min() 함수 (반복 가능한 데이터의 최댓값, 최솟값)
print(f"\n{'max(), min()':=^30}")
print(max([1, 2, 3]))
print(max("python"))

print(min([1, 2, 3]))
print(min("python"))

# oct() 함수 (정수를 8진수 문자열로 리턴)
print(f"\n{'oct()':=^30}")
print(oct(34))
print(oct(12345))

# open() 함수 (파일 객체 리턴) (r, w, a, b)
# f = open("file.txt","rb")

# ord() 함수 (유니코드 숫자값 리턴)
print(f"\n{'ord()':=^30}")
print('a')
print('가')

# pow(x, y) 함수 (x의 y제곱)
print(f"\n{'pow()':=^30}")
print(pow(2, 4))
print(pow(3, 3))

# range([start], stop, [step]) 함수 (반복 객체 함수)
print(f"\n{'range()':=^30}")
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0,-10,-3)))

# round(number, [소수점 자릿수]) 함수 (숫자를 반올림)
print(f"\n{'round()':=^30}")
print(round(4.6))
print(round(5.678, 2))

# sorted() 함수 (데이터를 정렬 후 리스트로 리턴)
print(f"\n{'sorted()':=^30}")
print(sorted([3, 1, 2]))
print(sorted(['a', 'b', 'c']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

# str() 함수 (문자열로 변환 후 리턴)
print(f"\n{'str()':=^30}")
print(str(3))
print(str('hi'))

# sum() 함수 (입력 데이터들의 합 리턴)
print(f"\n{'sum()':=^30}")
print(sum([1, 2, 3]))
print(sum((4, 5, 6)))

# tuple() 함수 (반복 가능데이터를 튜플로 변환하여 리턴)
print(f"\n{'tuple()':=^30}")
print(tuple('abc'))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# type() 함수 (자료형이 무엇인지 알려주는 함수)
print(f"\n{'type()':=^30}")
print(type("abc")) # 문자열 자료형
print(type([])) # 리스트 자료형
print(type(open("test",'w'))) # 파일 자료형

# zip() 함수 (동일한 개수로 이루어진 데이터 묶어서 리턴)
print(f"\n{'zip()':=^30}")
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list(zip(list_1, list_2)))
