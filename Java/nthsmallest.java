import java.io.*
import java.util.*
import java.text.*
import java.math.*
import java.util.regex.*

public class Solution{
  public static int NthSmallest(int[] arr, int nthSmallest){
    int temp=0;
    for(int i=0;i<arr.length-1;i++){
      for(int j=i+1;j<arr.length;j++){
        if(arr[i]>arr[j]){
          temp=arr[i];
          arr[i]=arr[j];
          arr[j]=temp;
        }
      }
    }
    return arr[nthSmallest-1];
  }
  public static void main(String args[]) throws Exception{
    Scanner sc=new Scanner(System.in);
    int size=sc.nextint();
    
    int[] arrNum=new int[Size]
    for(int i=0;i<size;i++){
      arrNum[i]=sc.nextInt();
    }
    int nthSmallest=sc.nextInt();
    
    System.out.println(NthSmallest(arrNum,nthSmallest));
      
  }
}
