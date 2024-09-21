#include <stdio.h>

int main(int argc, char *argv[])
{
  int i,j;
  int res;

  for(i=1; i<=5; i++)
    {
      for(j=1; j<=5; j++)
	{
	  res = i*j;
	  printf("%d X %d =%3d\n", i, j, res);
	}
    }
}
