def count(n):
    summa = 0
    for ii in range(1,n+1) :
        summa += ii
    return summa

if __name__ == "__main__":
    print(count(1)) # 1
    print(count(2)) # 3
    print(count(3)) # 6
    print(count(10)) # 55
    print(count(123)) # 7626