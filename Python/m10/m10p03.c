#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	char *first_block; 
	char *second_block; 
	char *third_block;

	first_block = (char *)malloc(100);
	second_block = (char *)malloc(100);
	third_block = (char *)malloc(100); 

	printf("[first_block] %p\n", first_block);
	printf("[second_block] %p\n", second_block);
	printf("[third_block] %p\n", third_block);
	
	strcpy(second_block, argv[1]); 
	free(second_block); 
} 
