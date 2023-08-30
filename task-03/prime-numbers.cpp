#include<iostream>
using namespace std;

int prime(int num){
    int counter=0,i;
    for (i=1;i<=num;i++){
        if (num%i==0){
            counter++;
        }
    }
    if (counter==2){
        return true;
    }
    else{
        return 0;
    }
}
int main(){
    int num2;
    int num=2;
    cout<<"Enter a number here : ";
    cin >>num2;
    while (num<=num2)
    {
        if (prime(num))
        {
            cout<<num<<" ";
        }
        num++;
    }
    
}