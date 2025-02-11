# 로또 게임
import random

def lotto():
    print("**환영합니다 로또 추첨기 입니다.**")
    select_num = input("원하는 추첨 번호를 눌러주세요.\n자동 : 1 | 수동 : 2\n")
    select_num = int(select_num)

    if select_num == 1 or select_num == 2 :
        if select_num == 1:
            user_input = list(range(1,46))
            user_num = random.sample(user_input, 6)

        elif select_num == 2:
            user_input = input("1 ~ 46까지 번호 6개입력 (공백사용) : ")
            user_num = [int(num) for num in user_input.split()]
            for i in user_num:
                if 0 < i < 47 and len(user_num) == 6:
                    pass
                else : 
                    print("잘못 입력하셨습니다.")
                    lotto()

        lotto_num = list(range(1,46))
        six_num = random.sample(lotto_num, 6)
        set_num = list(set(user_num) & set(six_num))
        correct = len(set_num)
        print(f"선택 수 : {user_num}")
        print(f"추첨 수 : {six_num}")

        if correct == 6:
            print("1등입니다.")
        elif correct == 5:
            print("2등입니다.")
        elif correct == 4:
            print("3등입니다.")
        elif correct == 3:
            print("4등입니다.")
        else: 
            print("낙첨")

    else: 
        print("잘못입력하셧습니다.")
        lotto()
     
lotto()