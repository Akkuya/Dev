#include <stdio.h>
#include <string.h>



void func(int *ptr, int row, int colm, int value) {
     
}


int main() {
    int my_array[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    func(&my_array[0], 1, 1, 7);
    return 0;
}