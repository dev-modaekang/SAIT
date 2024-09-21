#include <stdio.h>
#include <stdlib.h>

int my_atoi(char *strtxt)
{
  int retval = 0;
  while (*strtxt != '\0')
    {
      if (*strtxt < '0' || *strtxt > '9') // to remove the garbage values
	break;
      retval *= 10;            // to print out all values in the pointer(*)
      retval += *strtxt - '0';  // to print out 2 > 23 > 234 > 2345
      strtxt ++;
    }
  return retval;
}

int main(int argc, char *argv[])
{
  int i;
  int val=0;

  for (i=0; i<argc; i++) // i=1, we don't need if loop in the my_atoi function.
    {
      val+= my_atoi(argv[i]);   
    }
  printf("sum= %d \n", val);
  return 0;
}
