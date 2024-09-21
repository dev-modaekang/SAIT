#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 4

double rpnstack [MAXSIZE];
int rpnidx=0;
int check=0;

int main(int argc, char *argv[])
{
  int val;
  char *str = argv[0];
  char *ptoken;
  char *tail;
  double x,y,sum;
  int count = 0;
  while(1)
    {
      if(count ==0)
	{
	  printf("         .       : ");
	  ptoken = fgets(str, 80, stdin);
	  val = strtol(ptoken, &tail, 10);
	  rpnstack[rpnidx] = val;
	  count ++;
	}
      else
	{
	  printf("%16lf : ", rpnstack[rpnidx]);
	  ptoken = fgets(str, 80, stdin);
	  // if the value is number
	  if(*ptoken >= '0' && *ptoken <= '9')
	    {
	      val = strtol(ptoken, &tail, 10);
	      rpnidx++;
	      rpnstack[rpnidx] = val;
	    }
	  // if the value is operator
	  else
	    {
	      if(*ptoken == 'q' || *ptoken == 'Q')
		break;
	      // calculate area
	      x=rpnstack[rpnidx];
	      y=rpnstack[--rpnidx];
	      switch(*ptoken)
		{
		case '+':
		  sum=y+x;
		  rpnidx++;
		  rpnstack[rpnidx]=sum;
		  break;
		case '-':
		  sum=y-x;
		  rpnidx++;
		  rpnstack[rpnidx]=sum;
		  break;
		case '*':
		  sum=y*x;
		  rpnidx++;
		  rpnstack[rpnidx]=sum;
		  break;
		case '/':
		  sum=y/x;
		  rpnidx++;
		  rpnstack[rpnidx]=sum;
		  break;
		}
	      if(*ptoken == '\n')
		rpnidx++;
	    }
	}
    }
}
