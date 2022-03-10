#include <iostream>

using namespace std;

struct summa{
    int tulos = 0;
    void summaaja(int kierrosluku){
        
        for (int ii=1; ii<=kierrosluku; ii++){
            //cout << "kierros " << ii <<'\n';
            tulos = tulos+ii;
            //cout << tulos << '\n';
        }
    }
    void resettaaja(){
        tulos=0;
    }

    int arvo(){
        return tulos;
    }
};

int main(){

    int testiluvut [5] = {1,2,3,10,123};  // array


    // tähän looppi mikä testaa yks kerrallaan ton vastauksen
    summa aa;
    for (int ii=0; ii<5; ii++){
        aa.summaaja(testiluvut[ii]);
        cout << aa.arvo() << '\n';
        aa.resettaaja();     
    }
   
    return 0;

}