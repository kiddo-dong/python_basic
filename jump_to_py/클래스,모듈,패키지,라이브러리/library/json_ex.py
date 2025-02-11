#json 라이브러리
import json

with open("D:\\jump_to_py\\클래스,모듈,패키지,라이브러리\\library\\myinfo.json") as f:
    data = json.load(f)
    print(type(data))
    print(data)