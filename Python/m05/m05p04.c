#include <stdio.h>
#include <string.h>
#include <unistd.h>

unsigned long long get_stack(void)
{
    unsigned long long sp;
    asm("mov %%rsp, %0": "=rm"(sp));
    return sp;
}

int funbot(int a ,int  b , char *str)
{
  int add = a + b;
  printf("Address of funbot: %p\n", funbot);
  printf("[string] %s\n", str);
  

  int my_pid = getpid();
  char file_name[80];
  char line[240];

  char * token_a, token_b;

  //printf("funtop2 a%d b%d\n", a,b);
  FILE *file;
  sprintf(file_name, "/proc/%d/maps", my_pid);
  //printf("%s\n", file_name);
  file = fopen(file_name, "r");

  while(fgets(line, sizeof(line), file))
  {
    if(strstr(line, "stack") != NULL)
    {
      //printf("stack : %s", line);
      token_a=strtok(line, "-");
      token_b=strtok(NULL, " ");
      //printf("top:%s\n", token_b);
      break;
    }
  }

  unsigned long long * stackbase = (unsigned long long *) token_a;
  unsigned long long * stacktop = (unsigned long long *) token_b;
  unsigned long long * current_stack = (unsigned long long *)get_stack();

  //printf("top is %lx / base is %lx\n", stacktop, stackbase);
  //printf("current stack : %lx\n", current_stack);
  while(current_stack)
  {
    printf("%14.14p: 0x%16.16llx\t", current_stack++ , *current_stack);
    for(int j=0; j<=58; j+=8)
	  {
	    char character = (char)(*current_stack >> j & 0xff);
	    if(character >= ' ' && character <= 'Z' || character >= 'a' && character <= 'z')
	      printf("%c", character);
      else
        printf(".");
	  }
    printf("\n");
  }

  return add;	 
}

int funtop( int a, int b, char *str)
{  
  printf("Address of funtop: %p\n", funtop);
  //printf("funtop1 a%d b%d\n", a,b);
  a = a * 4;
  b = b * 2;
  //printf("funtop2 a%d b%d\n", a,b);

  int value = funbot(a,b,str);
  //printf("return is %d\n", value);
  return value;
}

int main (int argc, char **argv[])
{
  printf("Address of main  : %p\n", main);
  funtop(2, 2, "haha");
  return 0;
}
