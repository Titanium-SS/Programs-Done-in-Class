#include<iostream>
using namespace std;

void combination(auto arr, int n, int i = 0)
{
    if (i == n)
    {
        for (int j = 0; j < n; j++)
            cout << arr[j];
        cout << endl;
    }
    else
    {
        arr[i] = 'F';
        combination(arr, n, i + 1);
        arr[i] = 'T';
        combination(arr, n, i + 1);
    }
}

int main()
{
    char arr[4];
    cout << "The Truth Table combination is as follows: \n"; 
    combination(arr, 4);
}