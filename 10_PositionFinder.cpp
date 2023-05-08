#include<iostream>
using namespace std;

void display(int *arr, int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
}

int PositionPlacer(int arr[], int low, int high)
{
    int target = arr[low];
    int i = low + 1;
    int j = high;
    int temp;

    do
    {  while (arr[i] <= target)
        { i++;}

        while (arr[j] > target)
        {j--;}

        if (i < j)
        {   temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    while (i < j);
    temp = arr[low];
    arr[low] = arr[j];
    arr[j] = temp;
    return j;
}

int main()
{   
    int a[9]={6,3,1,2,4,8,7,9,5};
    int n = sizeof(a)/sizeof(a[0]);

    cout << "Before sorting: \n";
    display(a, n);

    PositionPlacer(a, 0, n-1);

    cout << "\nAfter sorting: \n";
    display(a, n);
    
    return 0;
}
