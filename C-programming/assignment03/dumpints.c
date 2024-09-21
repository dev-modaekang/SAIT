#include <stdio.h>

void dump_intx(void *addr, int count)
{
  int i;
  int *p = addr;
  for(i=0; i<count; i++){
      printf("%08x ", *p++ & 0xffffffff);
      if ((i%4)==3) //i&3 is same meaning //i%4==3 -> i=0 possible
	printf("\n");
  }
}

int main()
{
  char str[]= "Hello class, this is a very long string we will dump as bytes\n";
  dump_intx(str, 20);
  printf("\n");
}
