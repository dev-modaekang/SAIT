#include <stdio.h>

int main(void)
{
  int Kelvin, Celsius;

  for(Celsius = -270; Celsius <= 100; Celsius +=10)
  {
    Kelvin = Celsius + 273;
    printf("%4d %4d\n", Celsius, Kelvin);
  }
}
