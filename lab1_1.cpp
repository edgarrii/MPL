#include <stdio.h>
#include <iostream>

using namespace std;


 
int main () {
    
  int *arr = new int[5]{0, 1, 2, 3, 4};
  int t = 0;
  
  for (int i = 0; i < 5; i+=2) {
    if (i == 4) {
        break;
    }  
      
    t = arr[i];
    arr[i] = arr[i+1];
    arr[i+1] = t;

  }
  
  for (int i = 0; i < 5; i++) {
      cout << arr[i];
  }
  
 return 0;
}