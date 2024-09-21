#include <stdio.h>

#define LINELEN 80

int count=0;

int get_count(int some)
{
  while(some)
    {
      count++;
      some /= 10;
    }
  return count;
}

int main()
{
  int val=1;
  int i=1;
  
  while(count<LINELEN)
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
