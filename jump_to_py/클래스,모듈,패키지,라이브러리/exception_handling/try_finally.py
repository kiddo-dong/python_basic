# try-finally 문
# try 문에는 finally 절을 사용가능
# try 문 수행 도중 예외가 발생여부에 상관없이 항상 수행됨.

# 사용한 리소스를 close 할 때 많이 사용됨
"""
try :
    f = open.("트라이문.txt",'w')
    수행문장들

finally:     # 중간에 오류가 나더라도 무조건 실행됨
    f.close()
"""