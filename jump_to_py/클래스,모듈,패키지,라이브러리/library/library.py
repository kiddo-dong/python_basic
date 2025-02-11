# 표준 라이브러리


#datetime.date 라이브러리 (연,월,일 날짜표현)
print(f"\n{'datetime.date':=^30}")

import datetime

meetday = datetime.date(2023, 4, 12)
today = datetime.date(2024, 12, 4)

daymeet = today - meetday
print(f"만날 일 수 : {daymeet.days}")

day = datetime.date(2021, 12, 14)
print(f"요일입니다.(0 ~ 6) {day.weekday()}")
print(f'요일입니다. (1 ~ 7) {day.isoweekday()}')

# time 라이브러리 (시간관련)
import time
print(time.time())
print(time.localtime(time.time()))
print(f'현재시각 : {time.asctime(time.localtime(time.time()))}')
print(f'현재시간만 리턴가능 : {time.ctime()}')

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
'''
for i in range(1,11) :
    print(i)
    time.sleep(1)
'''
# math 라이브러리 
import math

print(f"최대공약수 : {math.gcd(60, 100, 80)}")
print(f"최소공배수 : {math.lcm(15, 25)}")

#random 라이브러리 (난수 발생)
import random

print(random.random())
print(random.randrange(1,10))
print(random.randint(1,55))

# 난수 pop 예제
import random

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == "__main__": 
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

# choice 사용
import random

def random_choice(data_choice):
    number_choice = random.choice(data_choice)
    data_choice.remove(number_choice)
    return number_choice

if __name__ == "__main__" :
    data_ch = [1,2,3,4,5]
    while data_ch :
        print(random_choice(data_ch))

# random.sample(섞을 변수, 갯수) 함수(리스트 무작위 섞기)
data = [1,2,3,4,5]
print(random.sample(data, len(data)))

# 로또 함수 제작
import random
def lotto():
    ball = list(range(1,46))
    lotto_list = random.sample(ball,6)
    return lotto_list
print(lotto())


# itertools.zip_longest (iterator, iterator, fillvalue = "채울 값")
# 리스트 병합 및 빈 요소 채우기
import itertools

student = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']
# result = zip(student, snacks)
# print(result)
result = itertools.zip_longest(student, snacks) # fillvalue 생략시 None으로 채움
print(list(result))
# EX) 2호선
import itertools

station = ["잠실", '잠실새내', "잠실나루"]
line = [2,2,2,2,2]
station_line = itertools.zip_longest(station, line, fillvalue = "역이름 없음")
print(list(station_line))

# itertools.permutations (중복없는 순열)
import itertools
permu = [1,2,3]
print(list(itertools.permutations(permu, 2)))

# itertools.product (중복 순열)
import itertools
produ = [1,2,3]
print(list(itertools.product(produ, repeat=2)))

# itertools.combination
import itertools
print(len(list(itertools.combinations(range(1,46), 6))))

# functools.reduce
import functools
data = [1,2,3,4,5]
result = functools.reduce(lambda x, y : x+y, data)
print(result)

# operator.itemgetter
from operator import itemgetter

student = [
("jane", 22, 'a'),
("dave", 32, 'b'),
("sally", 17,"c"),
]
result = sorted(student, key=itemgetter(1))
print(result)


suden_dic = [
    {"name" : "jain", "age" : 22, "grade" : 'A'},
    {"name" : "dave", "age" : 32, "grade" : 'B'},
    {"name" : "sally", "age" : 17, "grade" : 'C'},
]
result = sorted(suden_dic, key=itemgetter('age'))
print(result)

# shutil 파일복사 및 이동(백업파일)
import shutil
#shutil.copy("백업할 파일","파일 저장명")

# glob ( * 사용 시 )
import glob
glob.glob("경로\\찾고자하는 파일명")

# pickle