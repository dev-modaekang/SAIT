#include <stdio.h>
#include <stdlib.h>

#define COUNT 5
#define LINELENGTH 80

int count;

int get_count(int some)
{
  while(some)
    {
      count++;
      some /=10;
    }
  return count;
}

int main(int argc, char *argv[])
{
  int num=COUNT;
  int row, col;
  int check=1;
  int check2=1;
  int max;

  if (argc == 2)
    check = atoi(argv[1]);
  if(check == 0)
    num = 20;
  int pascal[num][num];
  int arr[num];

  pascal[0][0] = 1;
  pascal[1][0] = 1;
  pascal[1][1] = 1;
  arr[0] = 0;
  arr[1] = 1;

  for(row=2; row<num; row++)
    {
      pascal[row][0] = 1;
      for(col=1; col<row; col++)
	{
	  pascal[row][col] = pascal[row-1][col-1] + pascal[row-1][col];
	}
      pascal[row][row] = 1;
    }
  
  for(row=2; row<=num; row++)
    {
      count=0;
      max = row;
      if(check2==0)
	break;
      for(col=0; col<=row; col++)
	{
	  count = get_count(pascal[row][col]);
	  count++;
	  if(count > LINELENGTH-10)
	    check2 = 0;
	}
      arr[row] = (count-1)/2;
    }

  for(row=0; row<max; row++)
    {
      for(arr[row]; arr[max-1]-arr[row]>0; arr[row]++)
	{
	  printf(" ");
	}
      for(col=0; col<=row; col++)
	{
	    printf("%d ", pascal[row][col]);
	}
      printf("\n");
    }
}

