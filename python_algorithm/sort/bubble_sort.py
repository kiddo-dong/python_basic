# 버블 정렬 알고리즘

def bubble_sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1,i,-1):
            if x[j-1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]

def my_sort():
    print('| 버블 정렬 |')
    num = int(input("원소 개수를 입력 : "))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))
    return x

if __name__ == "__main__":
    x = my_sort()

    bubble_sort(x)

    print("| 정렬 완료 |")
    
    for i in range(len(x)):
        print(f"x[{i}] = {x[i]}")
