#include<iostream>
using namespace std;

int power(int base , int exponent) {
    if(exponent==0)
        return 1;
    if(base==0)
        return 0;    
    
    return (base*power(base, exponent-1));
}

int main() 
{
    int base;
    int exponent;

    cout << "Enter the base: ";
    cin >> base;
    cout << "Enter the exponent: ";
    cin >> exponent;

    cout << "Base raised to the exponent is: " << power(base, exponent);
}