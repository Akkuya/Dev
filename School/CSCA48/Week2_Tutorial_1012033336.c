#include <stdio.h>
#include <math.h>

int main()
{
    for (double i = 0; i < 2 * 6.18; i += 0.5)
    {
        float x = sin(i);
        int y = (x + 1) * 10; // Makes sin value positive, then scales accordingly

        for (int j = 0; j < y; j++)
        {
            printf(" ");
        }
        printf("*\n");
    }
    return 0;
}