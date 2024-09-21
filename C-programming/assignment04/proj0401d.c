#include <stdio.h>
#include <stdlib.h>

#define LINELEN 80

int count=0;

int get_count(int some)
{
  while(some)
    {
      count ++;
      some /= 10;
    }
  return count;
}

int main(int argc, char *argv[])
{
  int i=1;
  int val=1;
  int len;

  if(argc>1)
      len = atoi(argv[1]);
  else
      len = LINELEN;
  
  while(count<len)
  {
    get_count(val);
    if (i%2==1)
    {
      printf("%d ", val);
      val += 8;
      i++;
      count ++;
    }
    else
    {
      printf("%d ", val);
      val -= 4;
      i++;
      count++;
    }
  }
  printf("\n");
}
