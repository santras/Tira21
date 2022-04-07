#include <iostream>


using namespace std;

class Queenknight
{
private:
    int ruudut(int n,int x, int y){
        int osumat = 0; 
        // Map vei liikaa aikaa, ilmeisesti ordered c++:ssa. Yritetään 2 ulotteisella taulukolla
        int taulu[n][n];
        for(int ii=0; ii<=n; ii++){
            for(int jj=0; jj<=n; jj++){
                if (ii!=x or jj!=y){
                    taulu[ii][jj]=1;
                }
                else{
                    taulu[ii][jj]=0;
                }
                
            }
        }


        

        return 0;
    }

public:
    int count(int n)
    {
        if (n<3){               // Shakkkilauta liian pieni mahtumaan kuningatar ja ratsu
            return 0;
        }
        int laskuri =0;
        for (int ii=0; ii<=n; ii++){            // Mietitään tilanne jokaiselle hepan paikalle erikseen
            for (int jj=0; jj<=n; jj++){
              int maara = ruudut(n,ii,jj);          // Lasketaan kuningattaren mahdolliset paikat setupissa alifunktiossa
              laskuri = laskuri+maara;
            }

        }
        return laskuri;

    }
    
};





int main(){
Queenknight shakkiapu;
//cout<< shakkiapu.count(3)<< '\n';
cout<< shakkiapu.count(4)<< '\n';
//cout<< shakkiapu.count(5)<< '\n';
}

//if __name__ == "__main__":
//    print(count(3)) # 0
//    print(count(4)) # 40
//    print(count(5)) # 184