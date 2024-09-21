#include <ncurses.h>
#include <stdlib.h> // for exit() 
#include <stdio.h>
#include <unistd.h> // for usleep()
#define DELAY 100000 // microseconds

// initial screen to display the array with checking the screen size.
int draw_init(int size_rows, int size_cols)
{ 
  initscr();
  noecho(); // Don't display getch()
  curs_set(FALSE); //Don't display a cursor 
  int max_width = getmaxx(stdscr); // The maximum width of screen
  int max_height = getmaxy(stdscr); // The maximum height of screen
  
  if(max_height<size_rows || max_width<size_cols) // compare the size of screen
    {
      clear(); 
      move(max_height/2, max_width/2-10); // move to the middle of screen
      printw("windows is too samll\n"); 
      refresh();
      getch();
      endwin();
      exit(-1); //if screen is small, return -1
    }
}

// to shutdown the screen
void draw_finish(void)
{
   refresh();
   getch();
   endwin(); // Restore normal terminal behavior
}

// to display the alive cells on the screen
void draw_life(int rows, int cols,  short * state)
{
  int i, j;
  
  for(i=0; i<rows; i++)
    {
      for(j=0; j<cols; j++)
	{
	  move(i, j);
	  if(state[i*cols+j] & (1<<14))
	    printw("#");    
	  else
	    printw(" ");
	}
    }
  refresh();
  usleep(DELAY); // Shorter delay between movements
  clear(); // Clear the screen of all
}
