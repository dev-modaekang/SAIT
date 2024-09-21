#include <stdio.h>

int main(void)
{
  float fahr, cels;

  printf ("| fahr  | celus |\n");
  printf ("+-------+-------+\n");
  for(fahr=-40; fahr<=100; fahr+=10.)
  {
    cels = (fahr-32.) * 5./9.;

    printf ("| %5.1f | %5.1f |\n", fahr, cels);
    printf ("+-------+-------+\n");
  }  
}
