#include <stdio.h>

int main()
{
  //PART A
  char myname[] = "Modae Kang";
  char *p = (char *) &myname;
  
  while(*p != '\0')
    {
      printf("%c\t%3d\t0x%02x\n", *p, *p, *p);
      p++;
    }
}


