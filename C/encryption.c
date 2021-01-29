#include<stdio.h>
void main()
  {
    char array[100];
    int n;

    printf("Enter a string\n");
    scanf("%s", array);
    scanf("%d", &n);

    printf("Your string: %s\n", array);
    // return 0;

    int i=0;
    while(array[i]!='\0'){
      array[i]=array[i]+n;
      i=i+1;
    }
    printf("%s", array);
}
