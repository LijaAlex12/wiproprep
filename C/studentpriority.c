#include<stdio.h>
void main(){

  int a[10],b[10];
  int n,count,i,j;
  scanf("%d",&n);
  for(i=0;i<n;i++){
    scanf("%d",&a[i]);
  }
  b[0]=0;
  for(i=1;i<n;i++){
    count=0;
    for(j=i;j>0;j--){
      if(a[j-1]>a[i]){
        count=count+1;
      }
    }
    b[i]=count;
  }
for(i=0;i<n;i++){
  printf("%d",b[i]);
}
}
