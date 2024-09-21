#include <stdio.h>

#define SIZE 5

int main()
{
  int num[SIZE] = {11, 22, 33, 44, 55};
  int denom = 5;
  int k = 5;
  
  if (k < 0 || k > SIZE)
    printf("Error: Invalid number of elements (out-of-bounds).\n");
  else if (denom == 0)
    printf("Error: Donominator is zero.\n");
  else {
    int i;
    printf("Result of division by %4d: ", denom);
    for (i=0; i<k; i++)
      printf("%d ", num[i]/denom);
    printf("\n");
  }
}
