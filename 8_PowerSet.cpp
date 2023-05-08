#include<iostream>
using namespace std;


/* BACKTRACKING
void PowerSet(string str, int index=-1, string current=" ") {
    int n = str.length();

    if(index == n) return;

    cout << current << "\n";

    for(int i=index+1; i<n; i++) {
        current += str[i];
        PowerSet(str, i, current);
        current.erase(current.size()-1);
    }
    return;
}
*/

void PowerSet(string str, int index=0, string current=" ") {
    int n = str.length();

    if(index==n) {
        cout << " {";
        cout << current << " ";
        cout << "} ";

        return;
    }
    PowerSet(str, index+1, current+str[index]);
    PowerSet(str, index+1, current);
}

int main()
{
    string str="abc";
    cout << "The Power Set of the given string is: \n";
    cout << "{";
    PowerSet(str);
    cout << "}";
    return 0;
}