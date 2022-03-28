

def find(s):
    pituus=len(s)
    tulos=-1

    mahd_pituudet=[]
    s_set=set(s)
    if len(s_set)==1:   # poikkeustapaus kun kaikki samaa
        return (1)


    for ii in range(pituus-1,1,-1):                     # kokeillaan kaikki ]1,len(s)[  välissä olevat
        if pituus % ii == 0:    #jos menee tasan
            mahd_pituudet.append(ii)
    #print(mahd_pituudet)
    for jj in mahd_pituudet:                            # mahdollisille pituuksille omat testit esim 100 --> 50,25,20,10,5,4,2
        lista = []                                      # mahdolliset kirjainyhdistelmät esim ekalla kierroksella s[0:49] ja s[50:]
        listan_pituus = int(pituus/jj)                          # montako jäsentä listassa esim 2
        for ii in range(0,listan_pituus):
            lista.append(s[ii*jj:(ii+1)*jj])
        #print(lista, listan_pituus,jj)
        lista_set = set(lista)
        if len(lista_set)==1:       # kaikki listassa uniikkeja
            tulos=jj                # päivittyy pienemmäksi jos pienempiä löytöjä
    
    if tulos == -1:                 # ei löytöjä, joten itse lista pienin yksikkö
        return (pituus)
    else:
        return (tulos)






if __name__ == "__main__":
    #print(find("Bababadalgharaghtakamminapronnkonnbronntonnepronntuonnthunntrovarrhounawnskawntoohoohoordeenenthurnu"))
    print(find("aaaaa")) # 1  
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) #3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7