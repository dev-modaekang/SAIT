#include <stdio.h>

#define SEPARATOR()  printf("+----+----+----+----+----+----+\n");

int main(int argc, char *argv[])
{
  int row, col;
  int res;
  int numrows = 5;
  int numcols = 5;
  int line=0;

  for(row=0; row<=numrows; row++)
    {
      SEPARATOR()
      for(col=0; col<=numcols; col++)
	{
	  res = col*row;
	  if(row==0 && col ==0)
	    printf("|    ");
	  else if(row==0)
	    printf("|%3d ", col);
	  else if(col==0)
	    printf("|%3d ", row);
	  else
	    printf("|%3d ", res);
	}
      printf("|\n");
    }
  SEPARATOR()
}
