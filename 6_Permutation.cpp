#include<iostream>
using namespace std;

void swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}

int Perm(string& arr, int k, int n) {
    if(k==n)
            cout << arr << endl;    
    else {
        for ( int i=k; i<=n; i++) {
            swap(arr[i], arr[k]);
            Perm(arr, k+1, n);
            swap(arr[i], arr[k]);
        }
    }
}

int main()
{
    string str= "SINGH";
    int n = str.size();
    cout << "All possible permutations are: \n";
    Perm(str, 0, n-1);
    return 0;
}
