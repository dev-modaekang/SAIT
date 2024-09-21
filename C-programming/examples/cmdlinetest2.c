#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int val1=0;
  int i, j;

  for (i=1; i<argc; i++)
    {
      printf("%s", argv[i]);
    }
  printf("\t");
  for (j=1; j<argc; j++)
    {
      printf("%x ", *argv[j]);
    }
  printf("\n");
}
