import java.util.Scanner;

package com.vs-codes;

public class PrimeinRange{
    public static void main(String[] args) {
        int min=2,flag=0;
        int max;
        Scanner in =new Scanner(System.in);
        System.out.println("Enter the number : ");
        max=in.nextInt();
        for (int n=min;n<=max;n++){
            for (int i=2;i<n;i++){
                if (n%i==0){
                    flag=1;
                    break;
                }
            }
            if (flag==0){
                System.out.println(n+" ");
            }
            flag=0;
        }
    }
}