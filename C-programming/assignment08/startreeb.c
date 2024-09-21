#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int i, j;
  int num1 = atoi(argv[1]);
  int num2 = atoi(argv[2]);
  int num3 = atoi(argv[3]);

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

