
def create(n):
    lista = []

    for ii in range (1,n+1):
        if ii % 2 == 0:         # parillisille i:n arvoille
            lista = lista + [ii]
        else:
            lista = [ii] + lista
    return lista

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]