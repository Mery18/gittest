/*
 * ulamek.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;

class Ulamek {
private:
    int licznik;    
    int mianownik;
public:
    Ulamek(int, int);
    void zapisz( int, int);
    void wypisz(){
          cout << licznik << "/" << mianownik;
     }
     int get_l(){
            return licznik;
     }
     int get_m(){
            return mianownik;
     }
     void skracaj(); // metoda drukuje skrocona postać ułamka 
};

void Uolamek::skracaj() {
        ; // swykorzystaj algorytm nEuklidesa optymalny 
}

void Ulamek::zapisz(int l, int m){
    licznik = l;
    if(m!= 0) mianownik =  m;
    else {
            cout << ",mianownik nie może być zerem!";
            exit(1);
        }
    }
    
 Ulamek::Ulamek(int l, int m){
    licznik = l;
    if(m!= 0) mianownik =  m;
    else {
            cout << ",mianownik nie może być zerem!";
            exit(1);
        }
    }

int main(int argc, char **argv)
{
	
    //Ulamek  u1, u2;
    Ulamek u1(3, 7);
    Ulamek u2(1, 4);
    //u1.zapisz(3, 7);
    //u2.zapisz(1, 4);
    cout << "Ułamek 1: ";
    u1.wypisz();
    cout << endl << "Ułamek 2: ";
    u2.wypisz();
    
    u1.zapisz(7, 9);
    cout << "Licznik: " << u1.get_l() << endl;
    cout << "Mianownik: " << u1.get_m() << endl;
    
    Ulamek u3(u1.get_l(),u1.get_m());
    u3.wypisz();
    
	return 0;
}

