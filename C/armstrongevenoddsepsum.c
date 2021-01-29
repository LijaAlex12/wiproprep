#include<stdio.h>
#include<math.h>
void main(){
  int n,d[10],i=0,c=0,l,p,t,sum=0,a,k;
  scanf("%d",&n);
  p=n;
  t=n;
  while(p>0){

    p=p/10;
    l=l+1;
  }
  k=l-1;
  // printf("%d",l);
  while(n>0){
    a=n%10;
    d[k]=a;
    c=c+(int)pow(a,l);
    n=n/10;
    i++;
    k--;
  }
  if(t==c){
    i=0;
    sum=0;
    while(i<l){
      sum=sum+d[i];
      i=i+2;
    }
    printf("%d",sum);
  }
  else{
    i=1;
    sum=0;
    while(i<l){
      sum=sum+d[i];
      i=i+2;
    }
    printf("%d",sum);
  }


}
