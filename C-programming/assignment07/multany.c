#include <stdio.h>
#include <stdlib.h>

#define LENGTH 32

int count_num(int value)
{
  int count = 0;
  while(value>0)
    {
      value /= 10;
      count ++;
    }
  return count;
}

int main(int argc, char *argv[])
{
  char *str = argv[0];
  int a,b,c,x,z;
  int max;
  int i,j,k;
  int res;
  int num=5;
  
  if (argv[1])
    num = atoi(argv[1]);
  
  for(i=1; i<=num; i++)
    {
      for(j=1; j<=num; j++)
	{
	  max = num*num;
	  z = count_num(max);
	  x = count_num(num);
	  a = count_num(i);
	  for(a; (x-a)+1>0; a++)
	    {
	      printf(" ");
	    }
	  printf("%d X", i);
	  b=count_num(j);
	  for(b; (x-b)+1>0; b++)
	    {
	      printf(" ");
	    }
	  printf("%d =", j);
	  res = i*j;
	  c=count_num(res);
	  for(c; (z-c)+1>0; c++)
	    {
	      printf(" ");
	    }
	  printf("%d\n", res);
	}
    }
}
