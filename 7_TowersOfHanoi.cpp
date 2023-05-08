#include<iostream>
using namespace std;

void TOH(int n, char source, char destination, char mid) {
    if(n==0)
        return;

    TOH(n-1, source, mid, destination);
    cout << "Move disk " << n << " from rod " << source <<" to rod " << destination << endl;
    TOH(n-1, mid, destination, source);
}

int main()
{
    int n=5;
    cout << "The solution of the Towers Of Hanoi with "<< n << " disks is: \n";
    TOH(n, 'A', 'C', 'B');
    return 0;
}