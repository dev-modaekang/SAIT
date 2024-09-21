#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  int val1=0;
  int j;
  
  printf("argc= %d \n\n", argc);
  printf("&argc=%p &argv=%p",&argc, &argv);

  printf("\n");

  printf("argv=%p",argv);
  printf("\n");

 for (j=0; j<argc; j++)
    {
      
      printf("argv[%d]= %p ", j, argv[j]);
      printf("\n");
      //printf("At %p is %016lx %s\n",argv[j],(long int)*(argv[j]),argv[j]);
      printf("At %p is %016lx %s ",argv[j],*((long int*)argv[j]),argv[j]);

      printf("%02x ",*argv[j]);


      printf("\n");
    }
 



  
  for (j=0; j<argc; j++)
    {
      val1+= atoi(argv[j]);
      printf("Arg= %d %s ", j, argv[j]);
      printf("\n");
    }
  
  printf("Total Sum= %d \n",val1); 

}
