# 반복문 (while)
# 문장을 반복수행한다.
# 조건이 참인동안 while문에 속한 문장들이 반복해서 수행됨
'''
while 조건문 :
    수행문장1
    수행문장2
    수행문장3....
'''
# while 문을 이용하여 1~10 출력
num = 0
while num < 10 : # num은 0부터 9까지 반복 num < 10이면 문장을 빠져나감
    num+=1       # num = num + 1
    print(num)
    if num == 10: print("출력 완료")


# while문 만들기
prompt = """
1. ADD
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4:
        print(prompt)
        number = int(input())


# break
# break를 사용하면 while문을 빠져나갈 수 있다. 
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print(f"남은 커피의 갯수는 {coffee}개 입니다.")
    if coffee == 0:
         print("커피가 다팔림 , 판매중지")
         break
    

# coffee
coffee = 10
while True: #무한반복
    if money == 300:
        print('커피를 줍니다.')
        coffee = coffee - 1
    elif money > 300:
         print(f'거스름돈 {300 - money}을 주고 커피를 준다.')
         coffee = coffee - 1
    else : 
         print("돈 돌려줌")
         print(f'남은 커피 갯수{coffee}')
    if coffee == 0 :
         print('판매중지')
         break # 판매중지 시 break문 으로 while문 빠져나감
    
