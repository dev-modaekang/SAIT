#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int num;
  int i;

  while (1)
    {
      printf("Enter a number: ");
      scanf("%d", &num);
      if(num>=1)
	{
	  for(i=0; i<num; i++)
	    {
	      printf("*");
	    }
	  printf("\n");
	}
      else
	break;
    }
}
