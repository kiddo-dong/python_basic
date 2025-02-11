#무한 루프
# while의 조건문에 true를 입력하면 무한 반복이 가능하다.
# coffee 자판기
coffee = 10
while True : # 무한 루프
    money = int(input("커피는 300원 입니다. 돈을 넣어주세요 : "))
    if money == 300 :
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300 :
        print(f"거스름돈 {300 - money}원과 커피를 줍니다.")
        coffee -= 1
    elif money < 300 : 
        print("돈이 적습니다.")
        continue # while문의 첫문장으로 돌아간다.
    else :
        print("돈을 돌려줍니다.")
    if coffee == 0 :
        print("커피가 다 팔렸습니다. 판매종료")
        break # break 문으로 무한 루프 while문을 빠져나간다.
