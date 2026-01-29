#include <stdio.h>
#include <string.h>

void func1(int arr[], int size) {

    arr[0] = 100;
    return;
}

void func2(int *arr, int size) {
    arr[1] = 200;
    return;
}


int main()
{
    int arr[4];

    arr[0] = 10;
    arr[3] = 20;

    int array[4] = {10, 0, 0, 20};

    // Ways to initialize arrays

    /*
        - Same Data type
        - No Index Out of Bounds error
        - Negative indexing DOES work, but unpredictable result
        - Fixed size
    */

    // Strings = char[len(string) + 1]
    // Last item in the string is typically \0, the null delimeter.%d
    // The delimeter tells the computer that the rest of the array
    // is junk, many functions in <string.h> need this character.

    char str[1024] = "Hello";

    printf("%d\n", str[6]); // Idk if it will print but it is a valid character not junk.

    char test[1024];

    test[0] = 'A';
    test[7] = '\0';

    int x = strlen(test);

    printf("%d\n", x); // Prints 6, because the function uses \0 to determine the length.


    int a = 5;
    int *b = NULL;
    b = &a; // Assigns b the adress of a.

    print("%p\n", b); // Prints out the address.

    /*
    Passing arrays into functions does not make a copy, instead, the function gets the 
    ADDRESS of the first element, and can directly access and modify the array. This is called
    Pass-by-reference
    */
    return 0;

    int my_array[3] = {10, 20, 30};
    func1(my_array, 3); // {100, 20, 30}
    func2(my_array, 3); // {100, 200, 30}

    // Passing in my_array is the same as passing in &my_array[0], aka the address of the first
    // item.

    
}