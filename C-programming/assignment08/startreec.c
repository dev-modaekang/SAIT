#include <stdio.h>
#include <stdlib.h>

#define LENGTH 32

int main(int argc, char *argv[])
{
  char *str = argv[0];
  int i, j;
  printf("Enter rows: ");
  int num1 = atoi(fgets(str, LENGTH, stdin));
  printf("Enter height: ");
  int num2 = atoi(fgets(str, LENGTH, stdin));
  printf("Enter width: ");
  int num3 = atoi(fgets(str, LENGTH, stdin));

  if(num3%2 == 0)
   num3 += 1;
  
  for (i=1; i<=num1; i++)
  {
    for(j=1; j<=num1-i; j++)
	  {
	    printf(" ");
	  }
    for(j=1; j<=(2*i)-1; j++)
	  {
	    printf("*");
	  }
    printf("\n");
  }
  for (i=1; i<=num2; i++)
  {
    for(j=1; j<=num1-((num3/2)+1); j++)
	  {
	    printf(" ");
	  }
    for(j=0; j<=num3-1; j++)
	  {
	  printf("H");
	  }
    printf("\n");
  }
}

