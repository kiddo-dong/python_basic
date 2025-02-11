# 패키지
# 관련있는 모듈의 집합
# 패키지는 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해줌.

import sys
sys.path.append("D:\\jump_to_py")
print(sys.path)

import game.sound.echo
print(game.sound.echo.echo_test())

# __init__.py 의 용도
# __init__.py 파일은 해당 디렉터리(폴더)가 패키지의 일부임을 알려주는 역할
# 존재하지않으면 패키지 파일로 인식하지 못 함.

# __all__

# __init__.py에서 같은 디렉토리의 사용할 모듈을 정의해준다. 없으면 모듈이 사용 불가능하다.
# __all__ ['모듈파일명']
# 정의를 해줘야 다른 경로, 다른 파이썬 파일에서 사용이 가능하다.

# relative 패키지
# 패키지의 상속같은 느낌

# . - 현재 디렉터리 경로
# .. - 부모 디렉터리 경로