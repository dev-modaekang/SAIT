#include <stdio.h>
#include <stdlib.h>

#define LENGTH 32

int main(int argc, char *argv[])
{
  char *str = argv[0];
  int i,j;
  int res;
  int num=0;
  
  printf("Enter a number : ");
  num = atoi(fgets(str, LENGTH, stdin));
  
  for(i=1; i<=num; i++)
    {
      for(j=1; j<=num; j++)
	{
	  res=i*j;
	  printf("%3d X%3d =%4d\n", i, j, res);
	}
    }
}
