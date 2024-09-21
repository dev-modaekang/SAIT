#include <stdio.h>
#include <ncurses.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

#define DAY_WIDTH 11 // width of the day box
#define DAY_HEIGHT 4 // height of the day box
#define COL0 1 // left edge of Monday box
#define ROW0 3 // top edge of the first drawn week boxes

int max_width, max_height;
char *string[7] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
char *mon[12] = {"January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
char date_count[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
char message[] = "#error# need bigger screen!";
int lastday;
time_t timenow;
struct tm *ptm;

int last_location;
int first_location;
int first_row;
int lastday;
int year_increase=1900;
int last=56;
int first=34;
//int width[7] = {5, 9, 13, 17, 21, 25};
//int height[7] = {6, 17, 28, 39, 50, 61, 72};

void days(int row, int col, int width)
{
  int a, i, length;
  int j=0;
  for(i=0; i<7; i++)
    {
       length = strlen(string[i]);
       a = ((10-length)/2);
       move(row, col+j+a);
       printw("%s ", string[i]);
       j+=11;
    }
}

// print month & year on the top
void month_year(int row, int month, int width)
{
  int length_mon, year;
  char res[1];
  
  length_mon = strlen(mon[month]);
  move (row,(width-length_mon-4)/2);

  printw("%s  ", mon[month]);
  printw("%d", (ptm->tm_year)+year_increase);
  year = ptm->tm_year+year_increase;
  if((year%400==0 && year%100==0) || (year%4==0))
    date_count[1] = 29;
  else
    date_count[1] = 28;
  lastday = date_count[month];
}

void table(int row, int col)
{
  move(row-2, col-5);
  printw("+----------+");
  move(row-1, col-5);
  printw("|");
  move(row-1, col+6);
  printw("|");
  move(row, col-5);
  printw("|");
  move(row, col+6);
  printw("|");
  move(row+1, col-5);
  printw("|");
  move(row+1, col+6);
  printw("|");
  move(row+2, col-5);
  printw("+----------+");
}

// next month - print the date in the calendar
void date(int row, int col)
{
  int i, j;
  int date = 1;
  if(col==6)
    first_location = 72;
  else
    first_location = col-DAY_WIDTH;
  if(col>=39 || col==6)
    first_row = 21;
  else
    first_row = 25;
    
  if(date <=7)
    {
      while(col <= 72)
	{
	  move(row, col);
	  printw("%2d", date);
	  table(row, col);
	  date ++;
	  col+=DAY_WIDTH;	  
	}
    } 
  for(i=9; i<=25; i+=DAY_HEIGHT)
    {
      for(j=6; j<=72; j+=DAY_WIDTH)
	{
	  if(date>lastday)
	    break;
	  move(i, j);
	  printw("%2d", date);
	  table(i, j);
	  date++;
	  if(j==72)
	    {
	      last_location = 6;
	      last = last_location + 6;
	    }
	  else
	    {	
	      last_location=j+DAY_WIDTH;
	      last = last_location +6;
	    }
	}
    }
}

// previous month - print the date in the calendar
void date_p(int row, int col, int month) // col = first_location 
{
  int i, j;
  int date = date_count[month];

  if(col==72)
    last_location = 6;
  else
    last_location = col+DAY_WIDTH;
  while(1)
    {
      move(row, col);
      printw("%2d", date);
      table(row, col);
      date --;
      col-=DAY_WIDTH;
      if(col<6)
	break;
    }
  for(i=row-DAY_HEIGHT; i>=5; i-=DAY_HEIGHT)
    {
      for(j=72; j>=6; j-=DAY_WIDTH)
	{
	  if(date<1)
	    break;
	  move(i, j);
	  printw("%2d", date);
	  table(i, j);
	  date--;
	  if(j==6)
	    first_location = 72;
	  else
	    first_location=j-DAY_WIDTH;
	}
    }
  j+=DAY_WIDTH;
  if(j>=39 || j==6)
    first_row=21;
  else if (j==28 && date_count[month-1]==30)
    first_row=21;
  else if (j<=28 && (date_count[month-1]==28 || date_count[month-1]==29))
    first_row=21;
  else
    first_row = 25;
  move(max_height/2-1, max_width/2-1);
}

int main(int argc, char *argv[])
{
  int max_width, max_height, month, today_date, fist_date, key, check;
  
  initscr ();
  noecho();
  clear();

  max_width = getmaxx (stdscr);
  max_height = getmaxy (stdscr);
  
  if(max_width < 78 || max_height < 28)
    {
      if(max_width <= strlen(message))
	{
	  move(max_height/2, max_width/2-2);
	  printw("error");
	  refresh();
	  sleep(5);
	}
      else
	{
	  move(max_height/2, (max_width-strlen(message))/2-1);
	  printw(message);
	  refresh();
	  sleep(5);
	}
    }

  else
    {
      timenow = time(&timenow);
      ptm = localtime(&timenow);
      month = ptm->tm_mon; // month = 0~11
      today_date = ptm->tm_mday;

      // start to print value
      days(ROW0-1, COL0+1, DAY_WIDTH);
      month_year(ROW0-2, month, 78);
      if(month==10)
	date(5, 39); // November. 2018
      if(month ==11)
	date(5, 61); // December. 2018
      move(max_height-1, max_width-1);
      
      while(1)
	{ 
	  key = getch(); // q=113, Q=81, n = 110, N= 78, p=112, P=80
	  clear();
	  
	  //next month
	  if(key==110 || key ==78)
	    {
	      if(month==12)
		month = 12;
	      else
		month ++;
	      if(month ==12)
		{
		  month =0;
		  year_increase ++;
		}
	      days(ROW0-1, COL0+1, DAY_WIDTH);
	      month_year(ROW0-2, month, 78);
	      date(5, last_location);
	      move(max_height-1, max_width-1);
	      refresh();
	    }
	  
	  //previous month
	  else if(key==112 || key ==80)
	    {
	      if(month==0)
		{
		  month = 11;
		  year_increase --;
		}
	      else
		month --;
	      days(ROW0-1, COL0+1, DAY_WIDTH);
	      month_year(ROW0-2, month, 78);
	      date_p(first_row, first_location, month);
	      move(max_height-1, max_width-1);
	      refresh();
	    }
	  else if(key ==113 || key==81)
	    break;
	  else
	    printw("##Error!##\nput the correct value\n\n[EXAMPLE]\nn:next month\tp:previous month\tq:quit\n");
	}
    }
  refresh();
  endwin();
}
	   
