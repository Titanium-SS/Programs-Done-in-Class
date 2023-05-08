#include<iostream>
using namespace std;

int sum(int arr[], int n) {
    if(n==0)
        return  0;
    else {
        return ( sum(arr, n-1) + arr[n-1]);
    }
}

int main() 
{
    int arr[]={10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "The sum of the nos. in the array is: " << sum(arr, n);

    return 0;
}