#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSIZE 4

double rpnstack [MAXSIZE];
int rpnidx=0;
int check=0;
int decimal=0;

int check_value(double doubleval, int intval)
{
  float res;
  res = doubleval - intval;
  if (res == 0)
    return 0;
  else
    return 1;
}

int main(int argc, char *argv[])
{
  int i, val;
  char *str = argv[0];
  char *ptoken;
  char *tail;
  double x,y,sum;
  char *check;
  int count=0;

  if(argc >1)
    check = argv[1];
  if(strcmp(check, "-v")==0)
    {
      printf("[ ] :  ");
      ptoken = fgets(str, 80, stdin);
      val = strtol(ptoken, &tail, 10);
      rpnstack[rpnidx] = val;

      while(1)
	{
	  printf("[ ");
	  for (i=0; i<=rpnidx; i++)
	    {
	      decimal = check_value(rpnstack[i], rpnstack[i]);
	      if(decimal == 0)
		printf("%0.f ", rpnstack[i]);
	      else if(decimal == 1)
		printf("%.1f ", rpnstack[i]);
	    }
	  printf("] :  ");
	  ptoken = fgets(str, 16, stdin);
	  if(*ptoken >= '0' && *ptoken <= '9')
	    {
	      val = strtol(ptoken, &tail, 10);
	      rpnidx++;
	      rpnstack[rpnidx] = val;
	    }
	  else
	    {
	      if(*ptoken == 'q' || *ptoken == 'Q')
		break;
	      x=rpnstack[rpnidx];
	      y=rpnstack[--rpnidx];
	      switch(*ptoken)
		{
		case '+':
		  sum=y+x;
		  rpnstack[rpnidx]=sum;
		  break;
		case '-':
		  sum=y-x;
		  rpnstack[rpnidx]=sum;
		  break;
		case '*':
		  sum=y*x;
		  rpnstack[rpnidx]=sum;
		  break;
		case '/':
		  sum=y/x;
		  rpnstack[rpnidx]=sum;
		  break;
		}
	      if(*ptoken == '\n')
		rpnidx++;
	    }
	}
    }
  else
    {
       while(1)
	 {
	   if(count ==0)
	     {
	       printf("         .       : ");
	       ptoken = fgets(str, 16, stdin);
	       val = strtol(ptoken, &tail, 10);
	       rpnstack[rpnidx] = val;
	       count ++;
	     }
	   else
	     {
	       printf("%16lf : ", rpnstack[rpnidx]);
	       ptoken = fgets(str, 16, stdin);
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
		   x=rpnstack[rpnidx];
		   y=rpnstack[--rpnidx];
		   // calculate area
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
}
