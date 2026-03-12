#include <stdio.h>
#include <stdlib.h>
int main()
{
    int array[10];
    int d = 0;
    int *p;
    float *fp;
    // Fill the array with values
    // depending on if d=0 or
    // d=1 (unfortunately, it seems we
    // forgot to set d to some value!)
    if (d == 0) // Problem #0
    {
        for (int i = 0; i < 10; i++)
            array[i] = i;
    }
    else
    {
        for (int i = 0; i < 10; i++)
            array[i] = i * i;
    }
    // Print the array, unfortunately
    // we have an off-by-one error
    // in the for loop!
    for (int i = 0; i < 10; i++) // Problem #1
        printf("array[%d]=%d\n", i, array[i]);
    // Get a pointer to the array and use
    // it to change some values,
    // unfortunately we are trying to access
    // values that are not in the array
    p = &array[0];
    *(p + 4) = 15; // Problem #2
    // Let’s get some memory for floating point
    // data
    fp = (float *)malloc(5 * sizeof(float)); // 5 floats requested

    int *newarray = malloc(100 * sizeof(int));
    int sum = 0;
    for (int i = 0; i < 100; i++) {
        *(newarray + i) = 0;
        sum+=*(newarray + i);
    }    

    printf("Sum: %d\n", sum);

    free(newarray);
    // And the line below should crash the program
    // because we are trying to free memory for
    // an array that was not dynamically allocated!
    free(fp);  // Problem #3
    return 0; // All good?
    // No! we forgot to free() the memory assigned to
    // fp, so there is a memory leak!
    // Problem #4
}