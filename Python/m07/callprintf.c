#include <stdio.h>

char label[]="The address of main is ";

void
print_all (char *label,void *addr)
{  
    printf ("%s: 0x%08x\n", label,addr);
}

int
main (int argc, char **argv)
{  
    void *addr_of_main;  
    addr_of_main = (void *) &main;
    print_all (label,addr_of_main);  
    printf ("Done.");
}