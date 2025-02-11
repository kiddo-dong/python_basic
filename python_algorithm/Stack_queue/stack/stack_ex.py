
def push(x) :
    add_value = int(input("push 값 입력 : "))
    x.append(add_value)
    return x

def pop(x) :
    if x:
        x.pop()
    else: 
        print("stack is empty")
    return x

def dump(x) :
    if x:
        print(f"dump value : {x[len(x)-1]}")
    else :
        print("stack is empty")
    return x

def sort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1,i,-1):
            if x[j-1] > x[j]:
                x[j - 1], x[j] = x[j], x[j - 1]

    return x

if __name__ == "__main__":
    x = [] 
    while(True):
        print()
        print(f"x = {x}")
        print("| push:(1) | pop(2) | dump(3) | sort(4) | exit(0) |")
        num = input("입력 : ")
        if num == "1":
            push(x)
        elif num == "2":
            pop(x)
        elif num == "3":
            dump(x)
        elif num == "4":
            sort(x)
        elif num == "0":
            break;
        else :
            print("out of value")
    print("exit")