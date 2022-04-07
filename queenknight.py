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
    
    #print('summa alku ',sum(lauta.values()))

    # kuningatar ei saa olla samalla rivillä tai sarakkeessa kun heppa, koska kuningattaren siirrot 
    for ind in range(n):
        lauta[(x,ind)] = 0      # rivi
        lauta[(ind,y)] = 0      # sarake
    
    for ind in range(1,n):      # Kulmat
        #print(x+ind,y+ind)
        if (x+ind,y+ind) in lauta.keys():
            lauta[(x+ind,y+ind)] = 0
        #print(x+ind,y-ind)
        if (x+ind,y-ind) in lauta.keys():
            lauta[(x+ind,y-ind)] = 0
        #print(x-ind, y+ind)
        if (x-ind, y+ind) in lauta.keys():
            lauta[(x-ind, y+ind)] = 0
        #print(x-ind,y-ind)
        if (x-ind,y-ind) in lauta.keys():
            lauta[(x-ind,y-ind)] = 0

        
      

   # print('summa välissä ', sum(lauta.values()))

    # TÄSSÄ JOKIN VIRHE, EI MUUTA MITÄÄN 0:ksi
    #käydään läpi mahdolliset paikat
    for i in range(n):
        for j in range(n):
            if lauta[(i,j)] == 1:     # ei ole jo määritelty huonoksi
                #print(i,j)
                if abs(i-x)<3 and abs(j-y)<3:         #Hepan keskittämälle alueelle 5x5 ei mahdu kuningatar, eli ero ei saa olla alle 3
                    #print(i,j)
                    lauta[(i,j)] = 0
                #else:
                #for ind in range(3,n):
                #        if abs(x+ind) == abs(y+ind):            # kulmittain heppaan olevat eivät sovi koska kuningattaren viistosiirto 
                #            lauta[(i,j)] = 0
                 #           print(x,y,i,j,ind,x+ind,y+ind)

    #print(lauta)
    #print('summa loppu ', sum(lauta.values()))
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
    print(count(3)) # 0
    print(count(4)) # 40
    print(count(5)) # 184