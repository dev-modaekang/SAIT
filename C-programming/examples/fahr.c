// 1.5 A Numerical Example (page 5)

#include <stdio.h>

int main()
{
  int i;
  float fahr;
  float cels;

  

  printf ("+-------+-------+\n");
  for(fahr=-40; fahr<100; fahr+=10*9./5.)
  {
    cels = (fahr-32.) * 5.0/9.0;

    printf ("| %5.1f | %5.1f |\n", fahr, cels);
    printf ("+-------+-------+\n");
  }  
}
