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
  int val = 1;

  while(count<LINELEN)
    {
      get_count (val);
      printf("%d ", val);
      val *= 2;
      count ++;
    }
  printf("\n");
}
