#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int num;
  char arr;
  int i;

  while (1)
    {
      printf("Enter a number: ");
      scanf("%d", &num);
      if(num>=1)
	{
	  arr = 'A';
	  for(i=0; i<num; i++)
	    {
	      if(i%26 == 0 && i!=0)
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
