#include <iostream>
#include <set>
#include <string>

using namespace std;


class Sequence
{
public:
    int generate(int n)
    {
        int luku = 0;
        int kierros = 0;
        int tulos = 0;

        while(kierros<n){
            luku += 1;
            string luku_str = to_string(luku);
            set<char> set_char (luku_str.begin(), luku_str.end());   // https://www.includehelp.com/stl/converting-string-into-set-in-cpp-stl.aspx
            if (luku_str.length()>set_char.size()){
                kierros += 1;
                tulos = luku;
            }
        }
        return tulos;
    }

};  
    
    
    
int main()
{
Sequence generaattori;
cout << generaattori.generate(1) << '\n';
cout << generaattori.generate(2) << '\n';
cout << generaattori.generate(3) << '\n';
cout << generaattori.generate(10) << '\n';
cout << generaattori.generate(123) << '\n';
}
    
    
    
    
    /* print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505 */