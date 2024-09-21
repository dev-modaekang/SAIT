#include <stdio.h>
#include <stdlib.h>

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

int check_parameter(int check)
{
  int check_res;
  if(check>=2)
    check_res = check;
  else
    check_res = -1;
  return check_res;
}
  
int main(int argc, char *argv[])
{
  int i, j;
  int result=0;
  int err;
  int num=-1;

  if (argv[1])
      err = check_parameter(atoi(argv[1]));
  else
    err = -1;
  
  int prime[err];

  if(err == -1)
    printf("error\n");
  else
    {
      for(i=0; i<err; i++)
	{
	  prime[i] = i;
	}
      for (i=3; i<err; i++)
	{
	  for(j=2; j<i; j++)
	    {
	      if(prime[j] !=0)
		result = testone(prime[j], prime[i]);
	      if(result ==0)
		prime[i] = result;
	    }
	}
 
      for(i=0; i<err; i++)
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
      printf("\nThe number of prime numbers = %d\n", num);
    }
}


