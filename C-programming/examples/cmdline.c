#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int val;
  int i;
  printf("argc= %d \n", argc);
  for (i=0; i<argc; i++)
    {
      printf("arg= %d %s ", i, argv[i]);
      val= atoi(argv[i]);
      printf("val= %d", val);
      printf("\n");
    }
}
