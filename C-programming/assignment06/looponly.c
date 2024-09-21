#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int num;
  int limit=1;
  int count;
  int i;

  while (limit!=0)
    {
      printf("Enter a number: ");
      scanf("%d", &num);

      for(i=0; i<num; i++)
	{
	  count = i%10;
	  printf("%d", count);
	}
      limit = num;
      printf("\n");
    }
}
