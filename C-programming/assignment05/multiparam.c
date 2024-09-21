#include <stdio.h>

#define MAXMUL 10

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
  int numrows = MAXMUL;
  int numcols = MAXMUL;
  int line=4;

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
