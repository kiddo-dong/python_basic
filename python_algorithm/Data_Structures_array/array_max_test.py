# array_max import 하여 모듈 테스트
# max_of() 함수

from array_max import max_of

print("배열의 최댓값을 구합니다.")
print("주의 : End를 입력하면 종료됩니다.")

number=0
x = []

while True : 
    s = input(f"x[{number}]값을 입력하세요. : ")
    if s == "End":
        break
    x.append(int(s))
    number+=1

print(f"{number}개를 입력했습니다.")
print(f"최댓값은 {max_of(x)}입니다.")

# array_max.py안의 if __name__ = "__main__"은 실행이 안되는 것을 볼 수 있다.
