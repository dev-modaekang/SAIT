#include <ncurses.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h> 
#include <time.h> // for the random numbers

#define CELL_SIZE 1
#define MAX_ROWS 50 
#define MAX_COLS 200 
#define MIN_ROWS 24 
#define MIN_COLS 80 
#define DELAY 50000 

extern int draw_init(int size_rows, int size_cols);
extern void draw_life(int rows, int cols,  short * state);
extern void draw_finish(void);

char default_seed[MIN_ROWS][MIN_COLS] = {
"................................................................................",
"................................................................................",
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"........................................#.......................................",                                                                 
"......................................#.#.......................................",                                                                
"............................##......##............##............................",                              
"...........................#...#....##............##............................",                                                                 
"................##........#.....#...##..........................................",                                                                 
"................##........#...#.##....#.#.......................................",                                                               
"..........................#.....#.......#.......................................",                                                               
"...........................#...#................................................",                                                               
"............................##..................................................",                                                              
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                 
"................................................................................",                                                                
};    

int rows = MAX_ROWS;
int cols = MAX_COLS;
unsigned short state[MAX_ROWS][MAX_COLS]={0};
unsigned short storage[MAX_ROWS][MAX_COLS]={0};

int count_neighbors(int row, int col)
{
  int i,j;
  int count=0;
  
  for (i=-1;i<2;i++)
    {
      for(j=-1;j<2;j++)
	{  
	  //check every neighbour if live increase count
	  
	  if (i==0 && j==0)
	    continue;
	  
	  if(state [(row+i+rows)%rows][(col+j+cols)%cols]) //check the 14th bit(current generation) is alive or not
	    count++;
	}
    }

  return count;
}

// change the 15th bit for the next generation
void next_generation( void)
{
  int row,col;
  int count=0;
  int val=0;
  unsigned short new_generation[rows][cols]; 
  for(row=0;row<rows;row++)
    {
      for (col=0;col<cols;col++)
	{	  
	  count=count_neighbors(row, col);
	  
	  if(state[row][col]==1 )//check if the cell is live.
	    {
	      // any live cell with two or three live neighbours lives on to the next generation.
	      if (count==2 || count==3) 
		new_generation[row][col] =1; // change the 15th bit to 1.
	                      // any live cell with fewer than two or more than three live neighbours dies.
	      else
	        new_generation[row][col]=0; // change the 15th bit to 0.
	    }
	  else if (state[row][col]==0 ) // the dead cell
	    {
	      if(count==3)
		new_generation[row][col]= 1; // change the 15th bit to 1.
	      else
	        new_generation[row][col]= 0; // change the 15th bit to 0.
	    }
	  
	}
    }

  for(row=0;row<rows;row++)
    {
      for(col=0;col<cols;col++)
	{
	  state[row][col]=new_generation[row][col];
	  if (new_generation[row][col])
	    storage[row][col]=(storage[row][col]) | 0x8000;
	  else
	    storage[row][col]=(storage[row][col]) & 0x7fff;
	  storage[row][col]>>=1;
	}
    }
}

int stringcmp(char *str1,char *str2, int length)
{
  int i=0; 
  for(i; i<length; i++)
    {    
      if (*str1++!=*str2++)
	{
	  return 0;
   	  break;
	} 
    }
  return 1;
}

void initial_default(void)
{
  int i, j;
  for(i=0; i<MIN_ROWS; i++)
    {
      for(j=0; j<MIN_COLS; j++)
	{
	  if(default_seed[i][j]=='#')
	    {
	      state[i][j] = 1;
	      storage[i][j] = 0x7000;
	    }
	  else
	    {
	      state[i][j] = 0;
	      storage[i][j] = 0x0000;
	    }
	}
    }
}

void initial_random(void)
{
  int i,j;
  srand( (unsigned)time( NULL ) );
  for(i=0; i<rows; i++)
    {
      for(j=0; j<cols; j++)
	{
	  //generate a random number (0-16900),0x4000 is 16384 (14th bit =1)
	  state[i][j]=rand()%10;
	      
	  if (state[i][j]==1) 
	    {
		  storage[i][j]=0x7000;
	    }
	  else
	    {
	      state[i][j]=0;
	      storage[i][j]=0x0000;
	    }
	}
    }
}


 void print_storage()
 {
   int i;
   int row,col;
   for(row=0;row<rows;row++)
     {
       for(col=0;col<cols;col++)
	{
	  printf ("storage[%d][%d]=  %6d  ",row,col,storage[row][col]);
	  for(i=0;i<16;i++)
	    printf ("%3d",((storage[row][col])>>i)&1);
	  puts("");
	}
     }
   
 }
//FILE  This is an object type suitable for storing information for a file stream.
//FILE *fopen(const char *filename, const char *mode) opens the filename pointed to, by filename using the given mode,r-read,w-write.
//int fclose(FILE *stream)  Closes the stream. All buffers are flushed.
//size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)
//Reads data from the given stream into the array pointed to by ptr.


void initial_devrandom()
{
  int i ,j;
  unsigned int randval;
  FILE *f; 
  f = fopen("/dev/urandom", "r");     
  for(i=0; i<rows; i++)
    {
      for(j=0; j<cols; j++)
	{
	    fread(&randval, sizeof(randval), 1, f);
	  //generate a random number (0-16900),0x4000 is 16384 (14th bit =1)
	  state[i][j]=randval%2;
	  
	  if (state[i][j]==1) 
	    {
	      // state[i][j]=1;
		  storage[i][j]=0x7000;
	    }
	  else
	    {
	      state[i][j]=0;
	      storage[i][j]=0x0000;
	    }
	}
    }
   fclose(f);
}
//read data from txt file.
//each line contains two numbers for the coordinates(row col)
//deliminate by space
//char *strtok_r(char *str, const char *delim, char **saveptr);
void initial_fileseed(char *filename) 
{
FILE *f; 
  char *s; 
  char str[10];
  int i,j;
  char *ptoken=NULL; 
  char *psave=NULL;
  f = fopen(filename, "r");
  if (f==NULL)
    {
      perror("Error opening file");
      exit(-1);
    }
  while (1)
    {
      s=fgets(str,10, f); 
      if (s == NULL)
	break;
      else
	{
	  ptoken = strtok_r(str," ",&psave);
	  i=atoi(ptoken);
	  j=atoi(psave);
	}  
      state[i][j]=1;
      storage[i][j]=0x7000;
    }
 
  fclose(f);
}    
 
int main(int argc, char *argv[])
{ 
  short i,j;
  char *str;
  char key; 
  char *filename;
  if (argc<2)
      initial_default();  
  else
    {
      str=argv[1];
      if (str!=NULL)
	{
	  if (stringcmp(str,"--random",8)==1)
	    {
	      initial_devrandom();
	    }
	  else 
	    {
	      filename=str;
	      initial_fileseed(filename);
	    }
	    
	}  
    }
  
  draw_init(MIN_ROWS, MIN_COLS);

  if(draw_init(MIN_ROWS, MIN_COLS) == -1)
    exit;
  else
    {
      while(1)
	{
	  draw_life(rows,cols,*storage);
	  //      usleep(DELAY);
	  next_generation();
	  
	}
    }
} 

		
