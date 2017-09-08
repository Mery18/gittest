/*
 * witaj.cpp

 */


#include <iostream>

using namespace std;

int parzyste(int n)
{
    int i;
    for (i=0; i <=n; i+=2)
        cout<< i << " ";
    return i/2; 
}

int main(int argc, char **argv)
{
    int n;
    
    char tekst[20];
    cout <<"Witaj. Jak się nazywasz?";
    cin >> tekst;
    cout <<"Witaj" << tekst << endl;
    
    int lata;
    cout<< "Hej. Ile masz lat?" << endl;
    cin >> lata;
    cout <<"Urodziłeś się w " << 2017 - lata << endl;
    
    int data;
    data = 1983;
    if( data < 2017 - lata) 
    { cout <<"Jestem starszy :)"<< endl;
    }
    if( data > 2017 - lata) 
    { cout << "Jestem młodszy"<< endl;
	}
    if( data == 2017 - lata)
    { cout << "Mamy tyle samo lat!"<< endl;
        }
        
    
    cout << "Podaj liczbę: ";
    cin >> n;
    cout << "Parzystych: " << parzyste(n);
    
    return 0;
}

