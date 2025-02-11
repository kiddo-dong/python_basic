# 고정길이 스택 클래스를 사용
from enum import Enum
from Fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    s = [f'({m.value}).{m.name}' for m in Menu]
    while True:
        print(*s, sep = '', end="")
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
s = FixedStack(64)

