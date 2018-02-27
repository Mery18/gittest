/*
 * drzewo.cpp
 * 

 * 
 */


#include <iostream>
#include "drzewo.hpp"

using namespace std;

int main(int argc, char **argv)
{
    Wezel korzen;
    wezel.Dodaj(korzen, 10);
	wezel.Dodaj(korzen, 8);
	wezel.Dodaj(korzen, 4);
	wezel.Dodaj(korzen, 9);
	wezel.Dodaj(korzen, 20);
	wezel.Dodaj(korzen, 16);
	wezel.Dodaj(korzen, 30);
    korzen.Wyswietl();
    korzen.Usun();
    korzen.Wyswietl();
    
    
    
	
	return 0;
}

