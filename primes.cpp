#include <iostream>

using namespace std;

class Primes
{
public:
    int laskuri(int nn)
    {
        int montako = 0;
        for (int ii = 2; ii <= nn; ii++)
        {
            bool ohi = false;
            for (int jj = 2; jj < ii; jj++)
            {
                if (ii % jj == 0)
                {
                    ohi = true;
                }
            }
            if (ohi == false)
            {
                montako += 1;
            }
        }

        return montako;
    }
};

int main()
{
    int testiluvut[5] = {2, 10, 11, 100, 1000};
    Primes primelaskuri; // uusi primelaskuri
    for (int ii=0; ii<5; ii++){
        //cout << ii << ' ' << testiluvut[ii] << '\n';
        cout << primelaskuri.laskuri(testiluvut[ii]) <<'\n';
    }
    
    return 0;
}

// print(count(2)) #  1
// print(count(10)) # 4
// print(count(11)) # 5
// print(count(100)) # 25
// print(count(1000)) # 168