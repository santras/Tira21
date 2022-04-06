def ruudut(n,x,y):

    #Vaihtoehtojen määrä
    osumat = 0

    # Tehdään lauta dictionary jossa koordinaatit (x,y) avaimina ja 0 tai 1 arvoina (0=ei toimi, 1 toimii)
    lauta = {}

    # Alustetaan kaikki laudan arvot mahdollisiksi paikoiksi x kasvaa oikealle, y kasvaa alaspäin
    # tallennetaan koordinaatit tuple muodossa
    for i in range(n):
        for j in range(n):
            lauta[(i,j)] = 1
    
    print('summa alku ',sum(lauta.values()))

    # kuningatar ei saa olla samalla rivillä tai sarakkeessa kun heppa, koska kuningattaren siirrot (1)
    for ind in range(n):
        lauta[(x,ind)] = 0      # rivi
        lauta[(ind,y)] = 0      # sarake

    print('summa välissä ', sum(lauta.values()))

    # TÄSSÄ JOKIN VIRHE, EI MUUTA MITÄÄN 0:ksi
    #käydään läpi mahdolliset paikat
    for i in range(n):
        for j in range(n):
            if lauta[(i,j)] == 1:     # ei ole jo määritelty huonoksi
                if abs(i-x)<3 and abs(j-y)<3:         #Hepan keskittämälle alueelle 5x5 ei mahdu kuningatar, eli ero ei saa olla alle 3
                    #print(i,j)
                    lauta[(i,j)] = 0
                elif abs(x+i) == abs(y+j):            # kulmittain heppaan olevat eivät sovi koska kuningattaren viistosiirto
                    #print(x,y,i,j)
                    lauta[(i,j)] = 0

    print('summa loppu ', sum(lauta.values()))
    return sum(lauta.values())


def count(n):
    # Jos n=3 tai pienempi ei mahdu kentälle millään tavalla
    if n<=3:
        return 0

    # käydään läpi lauta niin että heppa on vuoron perään jokaisessa ruudussa ja lasketaan sitten kuningattaren mahdollisuudet sijoittua
    laskuri = 0
    for i in range(n):
        for j in range(n):
            maara = ruudut(n,i,j)       # Mietitään mahdollisten vaihtoehtojen määrä jokaiselle hepan sijainnille alifunktiossa
            laskuri= laskuri + maara
    
    return laskuri


if __name__ == "__main__":
    #print(count(3)) # 0
    print(count(4)) # 40
    #print(count(5)) # 184