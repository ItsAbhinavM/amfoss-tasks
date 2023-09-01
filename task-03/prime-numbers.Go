package main

// fmt package provides the function to print anything
import "fmt"

func printPrimeNumbersBeforeN(N int) {
   for i := 2; i <= N; i++ {
      isPrime := true
   for j := 2; j <= i/2; j++ {
      if i%j == 0 {
         isPrime = false
         break
      }
   }
   if isPrime {
         fmt.Println(i)
      }
   }
}
func main() {
   // declaring the variable N till which we have to find the Prime Numbers 
   var N int
   fmt.Println("Enter the value of N.")  
   fmt.Scanln(&N)   
   fmt.Println("The prime numbers between 1 to", N, "where N is included are  -")
   
   printPrimeNumbersBeforeN(N)
}