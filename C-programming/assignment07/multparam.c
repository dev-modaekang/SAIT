#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int i,j;
  int res;
  int num = atoi(argv[1]);

  for(i=1; i<=num; i++)
    {
      for(j=1; j<=num; j++)
	{
	  res = i*j;
	  printf("%2d X %2d =%4d\n", i, j, res);
	}
    }
}
