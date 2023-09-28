function findPrimeNumbers(lowerNumber, higherNumber) {
    console.log(`The prime numbers between ${lowerNumber} and ${higherNumber} are:`);

    for (let i = lowerNumber; i <= higherNumber; i++) {
        let isPrime = true;

        for (let j = 2; j < i; j++) {
            if (i % j === 0) {
                isPrime = false;
                break;
            }
        }

        if (i > 1 && isPrime) {
            console.log(i);
        }
    }
}

const lowerNumber = 2;
const higherNumber = parseInt(prompt('Enter higher number: '));

findPrimeNumbers(lowerNumber, higherNumber);
