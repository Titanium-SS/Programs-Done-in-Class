#include <iostream>
using namespace std;  
  
// Function to merge the subarrays of a[]  
void Merger(int a[], int beg, int mid, int end)    
{    
    int i, j, k;  
    int n1 = mid - beg + 1;    
    int n2 = end - mid;    
      
    int LeftArray[n1], RightArray[n2];  //temporary arrays  
      
    /* copy data to temp arrays */  
    for (int i = 0; i < n1; i++)    
        LeftArray[i] = a[beg + i];    
    for (int j = 0; j < n2; j++)    
        RightArray[j] = a[mid + 1 + j];    
      
    i = 0;              // initial index of first sub-array 
    j = 0;              // initial index of second sub-array   
    k = beg;            // initial index of merged sub-array/  
      
    while (i < n1 && j < n2)    
    {    
        if(LeftArray[i] <= RightArray[j])    
        {    
            a[k] = LeftArray[i];    
            i++;    
        }    
        else    
        {    
            a[k] = RightArray[j];    
            j++;    
        }    
        k++;    
    }    
    while (i<n1)    
    {    
        a[k] = LeftArray[i];    
        i++;    
        k++;    
    }    
      
    while (j<n2)    
    {    
        a[k] = RightArray[j];    
        j++;    
        k++;    
    }    
}    
  
void Sorter(int a[], int beg, int end)  
{  
    if (beg < end)   
    {  
        int mid = (beg + end) / 2;  
        Sorter(a, beg, mid);  
        Sorter(a, mid + 1, end);  
        Merger(a, beg, mid, end);  
    }  
}  

void printArray(int a[], int n)  
{  
    int i;  
    for (i = 0; i < n; i++)  
        printf("%d ", a[i]);  
    printf("\n");  
}
  
int main()  
{  
    int a[10]={2,3,5,7,9,1,4,6,8,10};
    int n = sizeof(a)/sizeof(a[0]);
    printf("Before sorting array elements are - \n");  
    printArray(a, n);  
    Sorter(a, 0, n - 1);  
    printf("After sorting array elements are - \n");  
    printArray(a, n);  
    return 0;  
}  