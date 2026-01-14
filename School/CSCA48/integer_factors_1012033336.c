#include <stdio.h>

int factor(int x, int y);

int main() {
  for(int i = 1; i <= 13; i++) {
    for(int j = 1; j <= i; j++) {
      int is_factor = factor(i, j);
      if (is_factor) {
        printf("y=%d is a factor of x=%d\n", j, i);
      }
    }
  }
}

int factor(int x, int y) {
  int sum = 0;
  for(int i = 0; i < x/y; i++) {
    sum += y;
    if (sum == x) {
      return 1;
    }
  }
  return 0;
}
