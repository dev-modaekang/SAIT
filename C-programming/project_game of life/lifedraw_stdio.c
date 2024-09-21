#include <stdio.h>
#include <ncurses.h>
#include <unistd.h>
#define DELAY 50000

#define CLSCR()  printf("\033[H\033[J") // clear the screen
#define GOTOXY(x, y) printf("\033[%d;%dH", x, y) // go to the coordinates x, y
#define HIDE() printf("\033[?25l") // hide the cursor

int draw_life (int rows, int cols, short *state)
{
  int i=0;
  int j=0;
  HIDE();
  // to display the alive cells on the screen
  for (i=0; i<rows;i++)
    {
      for (j=0;j<cols;j++)
	{
	  GOTOXY(i,j);
	  if ((state[i*cols+j]>>14)&1==1)
	    printf("*"); 
	  
	  else
	    printf(" ");
	  }
      
    }
  usleep(DELAY);
  CLSCR();
}


int draw_init (int size_rows, int size_cols)
{
  return 0;
}

void draw_finish()
{
  
}
