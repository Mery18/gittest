/*
 * szyfr_cezara.cpp
 *
 *
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)

{   char tekst[100];
	int klucz =3;
    cout << "Podaj tekst:"<< endl;
    cin >> tekst;
    cout <<"Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz);
    cout <<tekst;
	return 0;
}

