#include <stdio.h>

extern void
printproc(char state, int ppid, int pgid, unsigned long long mm_start_code, unsigned long long mm_end_code, unsigned long long mm_start_stack, unsigned long long esp, unsigned long long eip);

void 
main(void)
{
  printproc('S',123,456,4194304,
	    424508,140733872771840,140733872769048ULL,18446744071580841145ULL);
}
