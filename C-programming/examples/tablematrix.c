#include <stdio.h>
#include <stdlib.h>
#include <string.h>
	      
// print the dashes with function
void dashes(int numc, int numdashes)
{
  int i, j;
  for (i=0; i<numc; i++)
    {
      printf("+");
      for(j=0; j<numdashes; j++)
	{
	  printf("-");
	}
    }
  puts("+");
}

int main(int argc, char *argv[])
{
  char *str1;
  int row, col;
  int numrows=5;
  int numcols=5;
  int line=0;

  if(argc!=1)
    {
      if (argc==2)
	numrows = atoi(argv[1]);
      if (argc==3)
	{
	  numrows = atoi(argv[1]);
	  numcols = atoi(argv[2]);
	}
      if (argc==4)
	{
	  numrows = atoi(argv[1]);
	  numcols = atoi(argv[2]); //argument to integer '1' => 1
	  str1 = argv[3];

	  if(!strcmp(str1, "-d"))
	    line = 10;
	  else
	    line = 0;
	}
    }

  for(row=0; row<numrows; row++)
    {
      if(line!=0)
      dashes(numcols, line);
      for(col=0; col<numcols; col++)
	{
	  if(line!=0)
	  printf("|");
	  
	  printf("   [%d,%d]  ", row, col);
	}
      if(line!=0)
	puts("|");
      else
	printf("\n");
    }
  if(line!=0)
  dashes(numcols, line);

  printf("\n");
}
