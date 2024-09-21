#include <stdio.h>
#include <stdlib.h>

void dashes(int numc, int numdashes)
{
  int i, j;
  for (i=0; i<=numc; i++)
    {
      printf("+");
      for(j=0; j<=numdashes; j++)
	{
	  printf("-");
	}
    }
  puts("+");
}

int main(int argc, char *argv[])
{
  int row, col;
  int res;
  int numrows = 5;
  int numcols = 5;
  int line=4;

  if(argc>1)
    {
      if (argc==2)
	numrows = atoi(argv[1]);
      else if (argc==3)
	{
	  numrows = atoi(argv[1]);
	  numcols = atoi(argv[2]);
	}
    }

  for(row=0; row<=numrows; row++)
    {
      dashes(numcols, line);
      for(col=0; col<=numcols; col++)
	{
	  res = col*row;
	  if(row==0 && col ==0)
	    printf("|     ");
	  else if(row==0)
	    printf("|%4d ", col);
	  else if(col==0)
	    printf("|%4d ", row);
	  else
	    printf("|%4d ", res);
	}
      puts("|");
    }
  dashes(numcols, line);
}
