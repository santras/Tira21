def check(n):
     
    onnekas=False
    a=str(n)
    #print(len(a))

    summa=0
    for ii in range(0,len(a)):
        summa= summa+ int(a[ii])
    if summa%7==0:
        onnekas=True
    #print('summa ',summa)


    return onnekas

if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True