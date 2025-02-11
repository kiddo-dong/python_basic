# 1번
print(f"{'1번':=^30}")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i for i in numbers if i % 2 == 0]
print(result)

# 2번
print(f"{'2번':=^30}")
words = ["apple", "banana", "cherry", "date"]
result = [len(i) for i in words]
print(result)

# 3번
print(f"{'3번':=^30}")
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
result = [i for i in numbers if i**2 <= 100]
print(result)

# 4번
print(f"{'4번':=^30}")
first_names = ["John", "Jane", "Sam", "Anna"]
last_names = ["Doe", "Smith", "Brown", "Lee"]
result = [f"{first} {last}"for first,last in zip(first_names, last_names)]
print(result)

# 5번
print(f"{'5번':=^30}")
numbers = [12, -7, 5, -9, 0, -3, 6, 7]
result = [i for i in numbers if i < 0]
print(result)



