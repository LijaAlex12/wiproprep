#include<stdio.h>
int main(){
  char ch;
  scanf("%c",&ch);
//   directly to ascii
  if (ch>=65 && ch<=90)
      printf('upper');
  else if (ch>=97 && ch<=122)
      printf('lower');
  else if (ch>=65 && ch<=90)
      printf('number');
  else
      printf('symbol');
 return 0;
}
