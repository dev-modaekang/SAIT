#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int i;
  int val=0;

  for (i=0; i<argc; i++)
    {
      val+= atoi(argv[i]);   
    }
  printf("sum= %d \n", val);
}
