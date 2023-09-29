#include <iostream>
using namespace std;

bool isPrime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; ++i)
        if (num % i == 0) return false;
    return true;
}

int main() {
    int upperLimit;
    cout << "Enter an upper limit: ";
    cin >> upperLimit;

    cout << "Prime numbers between 2 and " << upperLimit << " are: ";
    for (int num = 2; num <= upperLimit; ++num)
        if (isPrime(num)) cout << num << " ";
    
    return 0;
}
