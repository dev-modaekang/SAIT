#include <stdio.h>

#define COUNT 100
#define LINELENGTH 80
int count=0;

int testone(int check_num, int candidate_num)
{
  if ((candidate_num % check_num) == 0)
    return 0;
  else
    return 1;
}

int get_count(int some)
{
  while(some)
    {
      count++;
      some /= 10;
    }
  return count;
}
  
int main(int argc, char *argv[])
{
  int i, j;
  int result=0;
  int num=-1;
  int prime[COUNT];

  for(i=0; i<COUNT; i++)
    {
      prime[i] = i;
    }
  for (i=3; i<COUNT; i++)
    {
      for(j=2; j<i; j++)
	{
	  if(prime[j] !=0)
	    result = testone(prime[j], prime[i]);
	  if(result == 0)
	    prime[i] = result;
	}
    }
 
  for(i=0; i<COUNT; i++)
    {
      if(prime[i] != 0)
	{
	  printf("%d ", prime[i]);
	  get_count(prime[i]);
	  num ++;
	  count ++;
	  if(count >= LINELENGTH)
	    {
	      printf("\n");
	      count=0;
	    }
	}
    }
  printf("\ncount=%d\n", num);
}
