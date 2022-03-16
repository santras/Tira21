#include <iostream>
#include <list>

using namespace std;

class Zigzag
{
public:
    string create(int n){
        string slista;
        for(int ii=1; ii<=n; ii++){
            if (ii % 2 == 0) {                 // parillinen
                slista = slista + to_string(ii);
            }
            else{
                slista = to_string(ii) + slista;
            }   

        }
        return slista;

    }

};




int main(){
    Zigzag zigzaglista; //uusi olio
    cout << zigzaglista.create(1) << '\n';
    cout << zigzaglista.create(2) << '\n';
    cout << zigzaglista.create(3) << '\n';
    cout << zigzaglista.create(4) << '\n';
    cout << zigzaglista.create(5) << '\n';


/* if __name__ == "__main__": python
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2, */

}


