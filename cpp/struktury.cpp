/*
 * struktury.cpp
 * 
 */


#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

struct osoba {
        char imie[50];
        char nazwisko[20];
        int wiek;
};

void wyswietlDane(osoba o) {
    cout << setw(20) << "Imię: " << o.imie << endl;
    cout << setw(20) << "Nazwisko: " << o.nazwisko << endl;
    cout << setw(20) << "Wiek: " << o.wiek << endl;
}

void zapiszDane(osoba t[], int ile){
    ofstream plik("osoby.txt", ios::app);
    if (plik.is_open()){
        cout << "Błąd otwarcia pliku!";
    } else{
        for(int i=0; i<ile; i++){
        cout << t[i].imie << "," << t[i].nazwisko<<","<< t[i].wiek << endl;
        plik << t[i].imie << "," << t[i].nazwisko<<","<< t[i].wiek << endl;
        }
    }
}

int czytajDane(osoba t[]){
    ifstream plik("osoby.txt");
    string linia;
    int i = 0;
    if (plik.is_open()) {
       while(getline(plik, linia)){
           cout << linia << endl;
           i++;
           } 
    } else {
        cout << "Błąð otwarcia pliku!";
    }
    return i;
    
}

//~int main(int argc, char **argv)
//~{
	//~osoba uczen1;
    //~cout << "Podaj imię: ";
    //~cin >> uczen1.imie;
    //~cout << "Podaj nazwisko: ";
    //~cin >> uczen1.nazwisko;
    //~cout << "Podaj wiek: ";
    //~cin >> uczen1.wiek;
    //~wyswietlDane(uczen1);
    
	//~return 0;
//~}


//~struct samochod{
        //~char marka[50];
        //~char kraj_pochodzenia[20];
        //~int przebieg[20];
//~};

//~void wyswietlDane(samochod o) {
    //~cout << setw(20) << "Marka: " << o.marka << endl;
    //~cout << setw(20) << "Kraj pochodzenia: " << o.kraj_pochodzenia << endl;
    //~cout << setw(20) << "Przebieg: " << o.przebieg << endl;
//~}

void getOsoby(osoba t[], int ile){
    
    for(int i=0; i<ile; i++){
        cout << "Podaj imię: ";
        cin >> t[i].imie;
        cout << "Podaj nazwisko: ";
        cin >> t[i].nazwisko;
        cout << "Podaj wiek: ";
        cin >> t[i].wiek;
        }
}

void drukujOsoby(osoba t[], int ile){
    
    for(int i=0; i<ile; i++){
        //cout << "Podaj imię: ";
        cin >> t[i].imie;
        //cout << "Podaj nazwisko: ";
        cin >> t[i].nazwisko;
        //cout << "Podaj wiek: ";
        cin>> t[i].wiek;
        }
}

int main(int argc, char **argv)
{   
    //~osoba uczen1;
    //~cout << "Podaj imię: ";
    //~cin >> uczen1.imie;
    //~cout << "Podaj nazwisko: ";
    //~cin >> uczen1.nazwisko;
    //~cout << "Podaj wiek: ";
    //~cin >> uczen1.wiek;
    //~wyswietlDane(uczen1);
    
	//~samochod auto1;
    //~cout << "Podaj marka: ";
    //~cin >> auto1.marka;
    //~cout << "Podaj kraj pochodzenia: ";
    //~cin >> auto1.kraj_pochodzenia;
    //~cout << "Podaj przebieg: ";
    //~cin >> auto1.przebieg;
    //~wyswietlDane(auto1);
    int ile;
    cout << "Ile osób? "; cin >> ile;
    osoba tb[ile];
    getOsoby(tb, ile);
	zapiszDane(tb, ile);
    cout << czytajDane(tb) << endl;
    
    return 0;
}
