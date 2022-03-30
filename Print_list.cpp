#include <iostream>
#include <list>

using namespace std;


class Print_list
{
public:
    void print(list<int> const &plista){
        for (auto const &i: plista){
            cout << i << endl;
        }
    }
};

int main(){
    list<int> lista;
    for (int ii=0; ii<=10; ii++){
        lista.push_back(ii);    
    }    

    Print_list printtaus;
    printtaus.print(lista);


}