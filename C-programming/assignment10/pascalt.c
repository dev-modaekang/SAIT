#include <stdio.h>
#include <stdlib.h>

#define COUNT 5
#define LINELENGTH 80

int count;

int get_count(int some)
{
  while(some)
    {
      count ++;
      some /=10;
    }
}

int main(int argc, char *argv[])
{
  int num=COUNT;
  int row, col;
  int check=1;
  int check2=1;

  if (argc == 2)
    check = atoi(argv[1]);
  if(check == 0)
    num = 20;
  int pascal[num][num];

  pascal[0][0] = 1;
  pascal[1][0] = 1;
  pascal[1][1] = 1;

  for(row=2; row<num; row++)
    {
      pascal[row][0] = 1;
      for(col=1; col<row; col++)
	{
	  pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col];
	}
      pascal[row][row] = 1;
    }
  
  for(row=0; row<num; row++)
    {
      count=0;
      if(check2==0)
	break;
      for(col=0; col<=row; col++)
	{
	  get_count(pascal[row][col]);
	  count ++;
	  printf("%d ", pascal[row][col]);
	  if(count > LINELENGTH-10)
	    check2 = 0;
	}
      printf("\n");	
    }
}
