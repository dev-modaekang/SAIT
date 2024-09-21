/* 1234 to  binary? */ 

#include <stdio.h>


int main()
{
  int bits[32];
  int mynum = 1234;
  int i=0;

  while (mynum)
    {
      bits[i++] = mynum & 1;
      printf("%d", mynum & 1);
      mynum /= 2;
    }
  printf("\n");
  
  while (--i>=0)
    {
      printf("%d", bits[i]); 
    }
  printf("\n\n");

  mynum=1234;
  // -------------------
  for (i=0; i<32; i++)
    {
      if(mynum & 0x80000000 )
	printf("1");
      else
	printf("0");
      mynum <<= 1;
    }
  printf("\n");
}



/* this code doesn't work
#include <stdio.h>

int main()
{
  int mynum = 1234; // 8 8 8 8 = 32
  int i;
 
  for(i=0; i<=32; i++); 
  {
    int rom = mynum % 2; 
    printf("%d", rom);

    if(mynum>0)
    {
      mynum /= 2;
      continue;
    }
    else
      break;
  }
  printf("\n");
}
*/


/*
 
#include <stdio.h>

int main()
{
  int mynum = 1234;
  int i;

  while (mynum)
    {
      printf("%d", mynum & 1);
      mynum /=2;
    }
  printf("\n");
}
*/
