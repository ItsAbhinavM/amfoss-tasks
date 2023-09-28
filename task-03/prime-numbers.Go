package main

import (
    "fmt"
)

func findAndPrintPrimes(N int) {
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
    var N int
    fmt.Println("Enter the value of N.")
    fmt.Scanln(&N)
    fmt.Println("The prime numbers between 1 to", N, "where N is included are -")

    findAndPrintPrimes(N)
}
