#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define N 100

// CSCA48 - Tutorial Exercise: Testing a program
//
// This program's goal is to:
//
// Generate the first 1000 prime numbers, store then im
// an array
//
// Once the first N (defined above) primes are stored, count how many
// times each of the digits from 0 to 9 happens to be the
// LAST (rightmost) digit in the prime numbers in the array.
//
// Print out these counts.

void findPrimes(int array[])
{
    // This function finds the first N prime numbers
    // and stores them in the array

    int idx = 0;
    int num = 2;
    int prime;

    while (idx < 100) // ISSUE: N is already defined, shouldn't hardcode 100.
    {
        prime = 1;
        for (int i = 0; i <= idx; i++) // ISSUE: Index out of bounds because of <=, and not <.
                                       // Additionally, this breaks the first iteration, which in turn breaks the whole program, 
                                       // Since all negative numbers are divisible by positive numbers by the modulo operator.
        {
            if (num % array[i] == 0)
                prime = 0;
        }
        if (prime)
        {
            array[idx] = num;
            idx++;
        }
        num++;
    }
}

int lastDigit(int n)
{
    // This function returns the last (rightmost) digit in
    // input number n - e.g. if the number is 25147, it returns 7

    char number[100];
    char lastDigit;

    sprintf(number, "%d", n);
    lastDigit = number[strlen(number) - 1]; // ISSUE: The length of number is 100, and there is no null terminator,
                                            // So the program is taking a garbage value.

                                            // A simple: return n % 10 would suffice.
    return lastDigit;
}

void countDigits(int counts[], int array[])
{
    // This function counts how many times each
    // digit appears as the final digit in one of
    // the first N primes
    for (int i = 0; i < N; i++)
        counts[lastDigit(array[i])]++;
}

int main()
{
    int primesArray[N];
    int digitCounts[10];

    for (int i = 0; i < N; i++)
        primesArray[i] = -1; // Mark this as unassigned
    
    // ISSUE: Digitcounts is not cleared, currently garbage.
    findPrimes(primesArray);

    // Count the last digits and print the counts!
    countDigits(digitCounts, primesArray);

    for (int i = 0; i < 10; i++)
        printf("Digit %d appears %d times as the last digit in these primes\n", i, digitCounts[i]);

    // No return value for main.
}