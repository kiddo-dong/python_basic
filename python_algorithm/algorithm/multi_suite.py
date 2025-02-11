# 복합문의 규칙
# 복합문의 스위트는 행마다 4개의 띄어쓰기 (tab)
a = 1
b = 2
if a < b :
    min2 = a
    max2 = b
if a < b : min2 = a
if a < b : min2 = a; max2 = b
if a < b : min2 = a; max2 = b; 
# if a < b : if c < d: x=u # 헤더와 같은 행에 복합문을 둘 수 없다.(오류 발생)