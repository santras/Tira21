# include <iostream>
# include <set>
# include <list>
#include <string.h>

using namespace std;

class Repeat
{
public:
    int find(string ss)
    {
        int pituus = ss.length();

        // Alustetaan määrä -1, joka merkkaa että pienempiä osakokonaisuuksia ei löytynyt
        int tulos = -1;                                 


        // Testataan, jos kaikki kirjaimet samoja, palautetaan koko pituus
        set<char> set_ss (begin(ss),end(ss));
        if (set_ss.size()==1)
        {
            return 1;  
        }


        // Listataan millä jaettaessa pituus menisi tasan ja tarkistetaan vain ne taukset
        list<int> lista_mahd_osapituuksista;
        for (int ii=pituus-1; ii>1; ii-- )          // katsotaan väliltä ]1,pituus[ 
        {                             
            if (pituus % ii == 0)
            {
                lista_mahd_osapituuksista.push_back(ii);
            }
        }
        //print(lista_mahd_osapituuksista);   

        // Testataan mahdolliset osapituudet erikseen        
        for (auto const &ii: lista_mahd_osapituuksista)
        {
            list<string> vali;
            int vali_maara = pituus/ii;
            for (int jj=0; jj<vali_maara; jj++)         // haetaan alkuperäisestä välit
            {           
                vali.push_back(ss.substr(jj*ii,ii));   
            } 
            
            // Muutetaan setiksi joka on uniikki tietorakenne
            set<string> vali_set(begin(vali), end(vali));
            if (vali_set.size()==1)             // päivittyy ensin isoimpaan osumaan ja sitten pienempiin
            {                        
                tulos = ii;
            }
        }

        // jos ei löydy pienempiä osakokonaisuuksia, palautetaan koko stringin koko, muuten pienin mahdollinen uniikki koko
        if (tulos == -1){                   
            return pituus;
        }
        return tulos;
    }
    
    // Apufunktio int listan printtaamiseen
    void print(list<int> const &plista)
    {
        for (auto const &i: plista){
            cout << i << endl;
        }
    }

    // Apufunktio string listan printtaamiseen
    void prints(list<string> const &plista)
    {
        for (auto const &i: plista){
            cout << i << endl;
        }
    }

};



int main()
{
    Repeat repeatteri;
    cout << repeatteri.find("aaa") << '\n';
    cout << repeatteri.find("abcd") << '\n';
    cout << repeatteri.find("abcabcabcabc") << '\n';
    cout << repeatteri.find("aybabtuaybabtu") << '\n';
    cout << repeatteri.find("abcabca") << '\n';
    //repeatteri.find("Bababadalgharaghtakamminapronnkonnbronntonnepronntuonnthunntrovarrhounawnskawntoohoohoordeenenthurnu");
    //repeatteri.find("Jaavakaapasaapas");
    //repeatteri.find("aaaabbbb");

    
    // print(find("aaa")) # 1
    // print(find("abcd")) # 4
    // print(find("abcabcabcabc")) # 3
    // print(find("aybabtuaybabtu")) # 7
    // print(find("abcabca")) # 7

    // printtifunktion testaus
    /* list<int> lista;          
    for (int ii=0; ii<=10; ii++){
        lista.push_back(ii);    
    }    
    repeatteri.print(lista); */
}