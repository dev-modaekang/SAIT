#include <stdio.h>
#include <windows.h>

int (*funptr)() = (void *) 0x75C1E5FD;

char program[] = "calc.exe";

int main()
{
    (*funptr)(program, 2);
}
