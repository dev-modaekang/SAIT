#include <stdio.h>

#define COUNT 10

int main(){
  unsigned int *p = (void *) main;
  int i, j, mask;
  
  for(i=0; i<COUNT; i++){
    printf("%p: 0x%08x ", p, *p);

      for(j=31; j>=0; j--){
	  mask=(1<<j);

	  if (((*p)&(mask)))
	    printf("1");
	  else
	    printf("0");
	  if (j%4 == 0)
	  printf(" ");
      }
      printf("\n");
      p++;
  }
}
