////////////////////////////////////////////////
// CSC A48 - Exercise 5 - Solving Magic Squares
//
// (c) F. Estrada
////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0

int isSolved(int unknown[], int len)
{
    for (int i = 0; i < len; i++)
    {
        if (unknown[i] >= 1)
        {
            return FALSE;
        }
    }
    return TRUE;
}

void solveRows(int magic[6][6], int length, int row_unknowns[], int row_sums[], int target, int col_unknowns[], int col_sums[])
{
    for (int i = 0; i < length; i++)
    {
        if (*(row_unknowns + i) > 1 || *(row_unknowns + i) == 0)
        {
            continue;
        }
        for (int j = 0; j < length; j++)
        {
            if ((*(magic + i))[j] == -1)
            {
                (*(magic + i))[j] = target - *(row_sums + i);
                *(row_unknowns + i) = *(row_unknowns + i) - 1;
                if (*(col_unknowns + j) >= 1)
                {
                    *(col_unknowns + j) = *(col_unknowns + j) - 1;
                    *(col_sums + j) = *(col_sums + j) + target - *(row_sums + i);
                }
                *(row_sums + i) = target;
            }
        }
    }
}

void solveColumns(int magic[6][6], int length, int col_unknowns[], int col_sums[], int target, int row_unknowns[], int row_sums[])
{
    for (int i = 0; i < length; i++)
    {
        if (*(col_unknowns + i) > 1 || *(col_unknowns + i) == 0)
        {
            continue;
        }
        for (int j = 0; j < length; j++)
        {
            if ((*(magic + j))[i] == -1)
            {
                (*(magic + j))[i] = target - *(col_sums + i);
                *(col_unknowns + i) = *(col_unknowns + i) - 1;
                if (*(row_unknowns + j) >= 1)
                {
                    *(row_unknowns + j) = *(row_unknowns + j) - 1;
                    *(row_sums + j) = *(row_sums + j) + target - *(col_sums + i);
                }
                *(col_sums + i) = target;
            }
        }
    }
}

void solveMagicSquare(int square[6][6])
{
    // This function receives an array of size 6x6
    // that corresponds to a magic square.
    // It then finds any entries with value -1
    // (which means they are not known),
    // and figures out what their value should
    // be to solve the magic square.
    //
    // Conditions:
    // You can not hard-code the value of the rows
    // and columns in the magic square - because
    // we will test this with a *different* magic
    // square than the one in this starter code
    //
    // Your function has to (somehow) figure out
    // what the sum of the rows and columns should be,
    // and then figure out for each entry whose
    // value is -1, what its value is to correctly
    // complete the magic square.
    //
    // This is about problem solving - you don't
    // need any fancy pointer management or anything
    // like that. Just plain old C with a 2D array
    // and a bit of thinking.
    //
    // As a reminder. 2D arrays in C are indexed as
    // array[i][j] - gives you the element at row i,
    // column j
    //////////////////////////////////////
    // TO DO: Complete this function
    //////////////////////////////////////
    int target_sum = 0;
    int row_sums[6] = {0, 0, 0, 0, 0, 0};
    int col_sums[6] = {0, 0, 0, 0, 0, 0};
    int row_unknown[6] = {0, 0, 0, 0, 0, 0};
    int col_unknown[6] = {0, 0, 0, 0, 0, 0};

    for (int i = 0; i < 6; i++)
    {

        int col_sum = 0;
        for (int j = 0; j < 6; j++)
        {
            if (square[j][i] == -1)
            {
                col_unknown[i]++;
            }
            else
            {
                col_sum += square[j][i];
            }
        }
        col_sums[i] = col_sum;
    }

    // First, find the target sum by checking rows without -1
    for (int i = 0; i < 6; i++)
    {
        int row_sum = 0;
        int has_missing = 0;
        for (int j = 0; j < 6; j++)
        {
            if (square[i][j] == -1)
            {
                has_missing = 1;
                row_unknown[i]++;
            }
            else 
            {
                row_sum += square[i][j];
            }
        }
        row_sums[i] = row_sum;
        if (!has_missing)
        {
            target_sum = row_sum;
        }
    }

    while (!isSolved(row_unknown, 6))
    {
        solveRows(square, 6, row_unknown, row_sums, target_sum, col_unknown, col_sums);
        solveColumns(square, 6, col_unknown, col_sums, target_sum, row_unknown, row_sums);
    }
}
// DO NOT MODIFY ANYTHING BELOW THIS LINE!
// (we mean it! the auto-checker won't be happy)
void printMagicSquare(int square[6][6])
{
    // Prints out the contents of a magic square 6x6
    int i, j, sum;
    for (i = 0; i < 6; i++)
    {
        sum = 0;
        for (j = 0; j < 6; j++)
        {
            printf("%03d, ", square[i][j]);
            sum = sum + square[i][j];
        }
        printf(" : %03d\n", sum);
    }
    printf("---------------------------\n");
    for (j = 0; j < 6; j++)
    {
        sum = 0;
        for (i = 0; i < 6; i++)
        {
            sum = sum + square[i][j];
        }
        printf("%03d, ", sum);
    }
    printf("\n");
}

#ifndef __testing // This is a compiler directive - used by the auto-checker to enable / disable this part of the code
int main()
{
    int magic[6][6] = {{32, 29, 4, 1, 24, 21}, {30, -1, 2, 3, -1, 23}, {12, 9, 17, 20, 28, 25}, {10, 11, 18, -1, 26, 27}, {13, -1, 36, 33, 5, 8}, {14, 15, 34, 35, 6, -1}};
    printMagicSquare(magic);
    printf("Solving Magic Square!\n");
    solveMagicSquare(magic);
    printMagicSquare(magic);
    return 0;
}
#endif