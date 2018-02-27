/*
 * drzewo2_main.cpp
 * 

 * 
 */


#include <iostream>
#include "drzewo2.hpp"

using namespace std;

int main(int argc, char **argv)
{
    Drzewo2 wezel;
    wezel.Dodaj( 10);
	wezel.Dodaj( 8);
	wezel.Dodaj( 4);
	wezel.Dodaj( 9);
	wezel.Dodaj( 20);
	wezel.Dodaj( 16);
	wezel.Dodaj( 30);
    wezel.WyswietlRosnoco();
    wezel.WyswietlMalejaco();
    
    
    
	
	return 0;
}
