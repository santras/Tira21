#include <iostream>
#include <string>

using namespace std;

class Lucky
{

public:
    Lucky(){
        
    }

    bool testeri(int n)
    {
        int summa = 0;
        string luku=to_string(n); 
        bool onnekas = false;

        
        for (int ii=0; ii<luku.size(); ii++){
            summa = summa + int(luku[ii])-48;            // char on oikeastaan lukuna ascii kirajain, ja lukuarvo saadaan vähentämällä 48
            //cout <<"luku " << int(luku[ii])-48 << " summa " << summa <<'\n';
        }

        //cout << "summa " << summa << " modulo " << summa%7 << '\n';
        if (summa % 7 == 0){
            onnekas=true; 
        }
        
        //cout << "summa "<< summa  <<'\n';

        return onnekas;
    }

};




int main(){
    Lucky onnilaskuri;
    cout <<"eka testi " << onnilaskuri.testeri(14) << '\n';
    cout << "toka testi " << onnilaskuri.testeri(16) << '\n';
    cout << "kolmas testi " << onnilaskuri.testeri(123) << '\n';
    cout << "neljas testi " << onnilaskuri.testeri(777) << '\n';
    cout << "viides testi " << onnilaskuri.testeri(9999999) << '\n';

    return 0;

}


/* if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True */