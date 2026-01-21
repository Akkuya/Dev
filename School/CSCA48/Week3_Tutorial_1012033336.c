#include <stdio.h>

float convert_to_degrees(float angle) {
    return angle*360.0/(2.0 *3.1415926535);
}
int main() {
    int x;
    float ang;
    x = 2;
    ang = convert_to_degrees(x);
    printf("%f\n", ang);
    return 0;
}

