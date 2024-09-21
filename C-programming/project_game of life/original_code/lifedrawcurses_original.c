#include <ncurses.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#define DELAY 150000

int draw_init(int size_rows, int size_cols)
{ 
  initscr();
  noecho();
  curs_set(FALSE); 
  int max_width = getmaxx(stdscr);
  int max_height = getmaxy(stdscr);
  
  if(max_height<size_rows || max_width<size_cols)
    {
      clear();
      move(max_height/2, max_width/2-10);
      printw("windows is too samll\n");
      refresh();
      getch();
      endwin();
      exit(-1);
    }
}

void draw_finish(void)
{
   refresh();
   getch();
   endwin();
}

void draw_life(int rows, int cols,  short * state)
{
  int i, j;
  short cell;
  
  for(i=0; i<rows; i++)
    {
      for(j=0; j<cols; j++)
	{
	  cell=(state[i*cols+j]>>14)&1;
	  move(i, j);
	  if(cell)
	    printw("#");    
	  else
	    printw(" ");
	}
    }
  refresh();
  usleep(DELAY);
  clear();
}
