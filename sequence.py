def generate(n):

    kierros = 0
    luku = 0
    tulos = 0
    
    while kierros<n:
        luku += 1
        luku_str = str(luku)
        luku_set = set(luku_str)

        if len(luku_str)>len(luku_set):
         kierros += 1
         tulos = luku
         
    return tulos


if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505