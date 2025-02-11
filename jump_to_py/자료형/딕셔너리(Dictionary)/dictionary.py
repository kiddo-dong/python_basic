# 딕셔너리 자료형
# 키(key)와 값(value)의 쌍으로 데이터를 저장
# 딕셔너리명 = {key1: Value1, Key2: Value2, ...}
# 데이터 베이스 처럼 데이터 값을 표현하기 좋음

# 딕셔너리
dic = {'name': '최동현', 'phone': '010-6691-6559', 'birth': '0207'} # 기본 형
a = {'li': [1, 2, 3]} # 딕셔너리에 리스트를 넣을 수 있다.

# 딕셔너리 쌍 추가
dic_ad = {1: 'a'}
a[2] = 'b' # 쌍 추가
print(a)

dic_ad_li = {1: 'a'} 
dic_ad_li[2] = ['b', 'c', 'd'] # 리스트 쌍 추가
print(dic_ad_li)

# 딕셔너리 변경
dic_ch = {1: 'a', 2: 'b'}
dic_ch[2] = 'BB' # 키값 2에 해당하는 값 BB로 변경
print(dic_ch)

dic_ch_li = {1: 'a', 2: ['b', 'c', 'd']}
dic_ch_li[2] = ['e','f'] # 키값 2에 해당하는 리스트를 변경
print(dic_ch_li)

# 딕셔너리 삭제
dic_de = {1: 'a', 2: 'b'}
del dic_de[2] # 키값 2 삭제
print(dic_de)

# 딕셔너리 중복 키
dic_key = {1: 'a', 1: 'b', 1: 'c'} # 중복 되는 키갑 존재 시, 마지막 키값으로 설정됨.
print(dic_key)

