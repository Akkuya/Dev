#include <stdio.h>

int main()
{
    int x, y;
    x = 5;
    y = 2;

    float result;

    result = (float)x / y;
    printf("%f\n", result);

    result = (float)x / (float)y;
    printf("%f\n", result);

    result = x / (float)y;
    printf("%f\n", result);

    result = x / y;
    printf("%f\n", result);

    return 0;
}