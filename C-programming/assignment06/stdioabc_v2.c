#include <stdio.h>
#include <stdlib.h>

#define LENGTH 32

int main (int argc, char *argv[])
{
  char *str = argv[0];
  int num;
  char arr;
  int i, j;

  while(1)
    {
      printf("Enter a number: ");
      num = atoi(fgets(str, LENGTH, stdin));
      
      if(num>=1)
	{
	  arr = 'A';
	  for(j=0; j<num; j++)
	    {
	      if(j%26 == 0 && j!=0)
		{
		  arr='A';
		  printf("%c", arr++);
		}
	      else
		printf("%c", arr++);
	    }
	  printf("\n");
	}
      else
	break;
    }
}
