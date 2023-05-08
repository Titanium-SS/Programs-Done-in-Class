#include<iostream>
using namespace std;

int Horner(int arr[], int n, int x, int i) {
    if(i==n)
        return arr[n];
    else 
        return (x*Horner(arr, n, x, i+1) + arr[i]);
}

int main() 
{
    int arr[]={1,2,3,4,5};
    int x;
    cout << "Enter the value of x: ";
    cin >> x;
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "The value of the expression is: ";
    cout << Horner(arr, n-1, x, 0);

    return 0;
}