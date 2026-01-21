#include <stdio.h>

int main() {
    int arr[]; // Errors

    float x[3];
    x[0] = 3.0;
    x[2] = 1.5;
    
    // Second item is garbage

    /*
    After a function is completed, the memory
    reserved is RELEASED, not ERASED. Meaning
    any other function can use the same registers
    for their variables.
    */

    int x = 4;
    int y = x;
    
    // Copies the value x, not referencing 
    // Same point in memory.
    return 0;
}