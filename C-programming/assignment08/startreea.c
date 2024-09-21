#include <stdio.h>

#define ROWS 10
#define TRUNK_HEIGHT 5
#define TRUNK_WIDTH 4

int i, j;
int num = TRUNK_WIDTH;

int main(int argc, char *argv[])
{
  if(num%2 == 0)
    num += 1;
  
  for (i=1; i<=ROWS; i++)
  {
    for(j=1; j<=ROWS-i; j++)
	  { 
	    printf(" ");
	  }
    for(j=1; j<=(2*i)-1; j++)
	  {
	     printf("*");
	  }
    printf("\n");
  }
  for (i=1; i<=TRUNK_HEIGHT; i++)
  {
    for(j=1; j<=ROWS-((TRUNK_WIDTH/2)+1); j++)
	  {
	    printf(" ");
	  }
    for(j=0; j<=num-1; j++)
	  {
	    printf("H");
	  }
    printf("\n");
  }
}

