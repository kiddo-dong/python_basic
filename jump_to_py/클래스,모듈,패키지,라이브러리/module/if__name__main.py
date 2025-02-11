import modprint1 # modprint1에 print()문이 있어 print문이 실행됨

print(modprint1.add(3,7))
# modprint1모듈의 if__name__ == "__main__": 문은
# import한 이 파이썬 파일에서 false로 작동한다. 

# __name__ 변수란?
# 파이썬이 내부적으로 사용하는 특별한 변수
# modprint1에서는 __name__ 변수에 __main__ 값이 저장되지만
# import 한 파일에서는 그 모듈의 이름이 저장된다.
print(modprint1.__name__)

