# 다른 디렉터리에 있는 모듈을 불러오는 방법 (othermod2)
# sys 모듈(파이썬 라이브러리 모듈)


# sys.path.append 사용하기
import sys
print(sys.path) # 파이썬 라이브러리의 디렉터리 목록을 보여줌
# sys.path에 모듈 추가
sys.path.append("D:\\jump_to_py\\othermod2") # sys.path에 apppend() 함수를 사용하여 라이브러리에 추가
print(sys.path) # 목록 출력


# PYTHONPATH 환경 변수 사용하기
'''
set PYTHONPATH = "D:\\jump_to_py\\othermod2"
'''