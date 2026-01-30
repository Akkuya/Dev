#include <stdio.h>
#include <math.h>

int main()
{
  int x;
  printf("%d\n", x); // Unexpected output, prints whatever was in memory

  x = 5.56;
  printf("%d\n", x); // Truncates the integer: DOES NOT ROUND;

  int a = 2;
  int b = 1;

  if (a & b)
  {
    printf("HELLO\n");
  }
  else
  {
    printf("WORLD\n");
  } // Prints WORLD

  // ANY NON-ZERO CHARACTER IS TREATED AS TRUE

  /*
    For loops can be iterated with

    ints, floats, AND chars
  */
  return 0;
}
