# zip() 함수

print(f'{"1번":=^30}')
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
print(list(zip(names, scores)))

print(f'{"2번":=^30}')
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]
print(dict(zip(keys, values)))

print(f'{"3번":=^30}')
list1 = [10, 20, 30]
list2 = [15, 25, 5]
result = [max(a,b) for a,b in zip(list1,list2)]
print(result)

print(f'{"4번":=^30}')
first_names = ["Tom", "Jerry", "Mickey"]
last_names = ["Cruise", "Mouse", "Mouse"]
result = [f"{a} {b}" for a,b in zip(first_names, last_names)]
print(result)

print(f'{"5번":=^30}')
products = ["Apple", "Banana", "Carrot", "Dates"]
prices = [1200, 800, 600, 1500]
result = [a for a,b in zip(products, prices) if b >= 1000]
print(result)