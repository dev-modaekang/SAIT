#include <stdio.h>

int main(){
  char *str = "\nModae Kang\n";
  int i=10;
  
  while (str[i])
    printf("%c", str[i--]);  
}
