#include <stdio.h>
#include <stdlib.h>

#define LENGTH 32

int main (int argc, char *argv[])
{
  char *str = argv[0];
  int num;
  int count;
  int i, j;

  while(1)
    {
      printf("Enter a number: ");
      num = atoi(fgets(str, LENGTH, stdin));
      
      if(num>=1)
	{
	  for(j=0; j<num; j++)
	    {
	      count = j%10;
	      printf("%d", count);
	    }
	  printf("\n");
	}
      else
	break;
    }
}
