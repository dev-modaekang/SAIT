#include <stdio.h>

char result;

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

// decorated character 
int opt_decorated(int character)
{
  if(character==0)
    result = 'N';
  else if (character!=0)
    result = 'Y';
  //else if (colval==0)
  //  col_res = 'N';
  //else if (colval!=0)
  //  col_res = 'Y';
  return result;
}

int main(void)
{
  int row, col;
  int numrows=5;
  int numcols=5;
  char row_res, col_res;

  // normal matrix
  for(row=0; row<numrows; row++)
    {
      dashes(numcols, 10);
      for(col=0; col<numcols; col++)
	{
	  printf("|");
	  printf("   [%d,%d]  ", row, col);
	}
      puts("|");
    }
  dashes(numcols, 10);

  printf("\n\n");
  
  // decorated
    for(row=0; row<numrows; row++)
    {
      dashes(numcols, 10);
      for(col=0; col<numcols; col++)
	{
	  printf("|");
	  row_res = opt_decorated(row);
	  col_res = opt_decorated(col);
	  printf("   [%c,%c]  ", row_res, col_res);
	}
      puts("|");
    }
  dashes(numcols, 10);
  
}



// print the dash without function
/*
int main(void)
{
  int row, col;
  int numrows=LIMIT;
  int numcols=LIMIT;

  for(row=0; row<LIMIT; row++)
    {
      printf("+-----------+-----------+-----------+-----------+-----------+\n");
      for(col=0; col<LIMIT; col++)
	{
	  printf("|   [%d,%d]   ", row, col);
	}
      puts("|");
    }
   printf("+-----------+-----------+-----------+-----------+-----------+\n");
}
*/
