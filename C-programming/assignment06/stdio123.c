#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int num;
  int count;
  int i;

  while (1)
    {
      printf("Enter a number: ");
      scanf("%d", &num);
      if(num>=1)
	{
	  for(i=0; i<num; i++)
	    {
	      count = i%10;
	      printf("%d", count);
	    }
	  printf("\n");
	}
      else
	break;
    }
}
