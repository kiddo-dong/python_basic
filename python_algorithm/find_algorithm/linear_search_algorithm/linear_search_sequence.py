# linear_serch() 함수 이용하여 뮤터블 객체들 선형 검색

from linear_search_for import linear_serch

tu = (4, 7, 5.6, 2, 3.14, 1)
st = "string"
li = ['DTS', 'AAC', 'FLAC']

print(f'{tu}에서 5.6의 인덱스는 {linear_serch(tu, 5.6)}')
print(f'{st}에서 "n"의 인덱스는 {linear_serch(st, "n")}')
print(f'{li}에서 "DTS"의 인덱스는 {linear_serch(li, "DTS")}')