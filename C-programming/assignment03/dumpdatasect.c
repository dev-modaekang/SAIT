#include <stdio.h>

char myname[] = "Modae Kang";
char alphabet[] ="ABCDEFGHIJKLMNOPQRSTUVWSXYZ";

extern void *__data_start;
extern void *_edata;

unsigned int *pbegin = (void *) &__data_start;
unsigned int *pend = (void *) &_edata;

int main (int argc, char *argv[])
{
  int i,j;
  for(pbegin; pbegin <= pend; pbegin++)
    {
      printf("%p: 0x%08x ", pbegin, *pbegin);
      
      for(i=31; i>=0; i--)
	{
	  if((*pbegin)&(1<<i))
	    printf("1");
	  else
	    printf("0");
	  
	  if((i%4)==0)
	    printf(" ");	  
	}
      
      int mask=0xff;
      for(j=24; j>=0; j-=8)
	{
	  char character = (char)(mask & (*pbegin>>j));
	  
	  if(character >= ' ' && character <= 'Z' || character >= 'a' && character <= 'z')
	    printf("%c", character);
	}
      
      printf("\n");
    }
}
