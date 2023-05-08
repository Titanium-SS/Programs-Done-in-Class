#include<iostream>
using namespace std;

int Selector(int arr[], int i, int j) {
    if(i==j)                                //Compares index of selected element with the no. of elements in then array 
        return i;
    else {
        int k = Selector(arr, i+1, j);      //repeatedly find the index of the smallest no. in the array
        return (arr[i]<arr[j])?i:k;         //return the index of the selected or the compared element
    }
}

void Sorter(int arr[], int n, int ind=0) {  //ind=0 to select the first element to initiate
    if(ind==n) return;                      //if the array is empty move out
    else
    {
        int k = Selector(arr, ind, n-1);    //store the index of the smallest element in variable k

        //swaping begins when condition is met
        if(k != ind) { 
            int temp = arr[k];     
            arr[k] = arr[ind];
            arr[ind] = temp;
        }
    }
    Sorter(arr, n, ind+1);                 //Sort for the the next no. hence ind is incremented
}


int main()
{
    int arr[]={99,14,36,101,440,56,99,78};
    int n = sizeof(arr)/sizeof(arr[0]);

    Sorter(arr, n, 0);

    for (int i = 0; i < n; i++)
        cout << arr[i] <<" ";

    return 0;
}

