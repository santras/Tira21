
def find(s):
    # TODO
    # kohta 1 mietitty, seuraavaksi kohta 2 ja sitten yleistäminen
    # 1. etsi eka kirjain lopuista - jos yhtä monta kuin length->tulos 1
    #                              - jos ei yhtään -> tulos length 
    # 2. etsi toka kirjain lopuista - jos yhtä monta kuin length/2 -> tulos 2
    #                               - jos ei yhtään -> tulos length
    # 3. etsi kolmas kirjain lopuista -jos yhtä monta kuin length/3 -> tulos 3
    #                               - jos ei yhtään -> tulos length
    # jne

    if len(s)==1:           # Yhden pitunen
        return 1

    if s.find(s[0],1,len(s))==-1: # eka kirjain ei esiinnyt uudelleen
        return (len(s))

    else:
        substringit=[]   # alkukohdat matcheille
        matchiluku =0
        viela=True
        ii=0
        while ii != len(s):                  # kun ei olla lopussa
            if s.find(s[0],ii,len(s)) == -1: # kierros loppuu, ei enää matcheja
                break
            else:
                loyty_ind = s.find(s[0],ii,len(s))
                substringit[matchiluku]= loyty_ind
                matchiluku += 1
                ii = loyty_ind + 1
        
        if matchiluku == len(s):
            return 1
        

            


    #for ii in range(1,len(s)):
    #    if s.find(s[ii-1],ii,len(s))==-1: # ei matchia (ei saa tulla tähän jos löytyy kaava, vain jos joku kirjain ei esiinny ollenkaan uudelleen)
    #        return (len(s))
    #    else:
    #        for jj in range(0,len(s)):





        #print (ii)
        #print(s[ii])
        #print(s.find(s[ii],ii,len(s)))
        #print(s.find('b',ii,len(s)))                # jos löytyy indeksi, jos ei -1
        #if s.find(s[ii-1],ii,len(s))==-1:     # ei löydy uutta matchia
        #    print('hep')


if __name__ == "__main__":
    #print(find("aaaaa")) # 1  3a
    print(find("abcd")) # 4
    #print(find("abcabcabcabc")) # 3
    #print(find("aybabtuaybabtu")) # 7
    #print(find("abcabca")) # 7
