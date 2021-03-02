import java.uitl.*

public class MyClass{

  Boolean isCorrect(int n){
  int sq=n*n;
  while(n>0){
  if(n%10!=sq%10)
      return false;
  p=p/10;
  sq=sq/10;
  
  }
  }
public static void main(String args[]){  
MyClass t=new MyClass();
Scanner sc=new Scanner(System.in);
int p=sc.nextInt();

if(p>0)
{
  if(t.isCorrectNum(p)){
  System.out.println('correct Number');
  else{
  System.out.println('incorrect Number');
  }
}

else{
System.out.println('wrong Input');
}

