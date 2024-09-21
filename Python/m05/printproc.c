#include <stdio.h>

void printproc(char state, int ppid, int pgid, unsigned long long mm_start_code, unsigned long long mm_end_code, unsigned long long mm_start_stack, unsigned long long esp, unsigned long long eip) 
{
	printf("State:      %18c\n", state);
	printf("ParentPid:  %18d\n", ppid);
	printf("ParentGid:  %18d\n", pgid);
	printf("StartCode:  0x%.16llx\n", mm_start_code);
	printf("EndCode:    0x%.16llx\n", mm_end_code);
	printf("StartStack: 0x%.16llx\n", mm_start_stack);
	printf("ESP:        0x%.16llx\n", esp);
	printf("EIP:        0x%.16llx\n", eip);
}	