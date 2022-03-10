def count(n):
    montako=0
    for ii in range(2, n+1):
        #print('ii',ii)
        ohi=False
        for jj in range(2, ii):
            
            #print('ii,jj,ii/jj',ii,jj,ii/jj)
            if ii%jj == 0:
                ohi = True
            #print(ohi)
        if not ohi:
            #print('lisäys')
            montako+=1

    return montako


if __name__ == "__main__":
    print(count(2)) #  1
    print(count(10)) # 4
    print(count(11)) # 5
    print(count(100)) # 25
    print(count(1000)) # 168