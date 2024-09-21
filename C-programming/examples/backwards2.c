#include <stdio.h>
#include <string.h>

int main(){
  char *str = "\nModae Kang Thanks\n";
  int i = 17;
  
  while (str[i])
    printf("%c", str[i--]);  
}
