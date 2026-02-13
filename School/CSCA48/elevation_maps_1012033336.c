/*
 * CSC A48 - Exercise 6
 * (c) F.J. Estrada
 *
 * You DO NOT NEED TO READ OR UNDERSTAND the image
 * reading/writing functions 'writePGMimage' and
 * 'readPGMimage'.
 *
 * Feel free to skip them! and go directly to the
 * extract_levelset() function which is where you
 * need to do your work (it's just above main() ).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void writePGMimage(unsigned char *image, int size_x, int size_y)
{
    // Output a PGM image map from the specified array. It is assumed
    // the array has size (size_x x size_y) and is of type unsigned char.
    // The output file is 'output.pgm'

    FILE *f;
    f = fopen("output.pgm", "wb");
    if (f != NULL)
    {
        fprintf(f, "P5\n");
        fprintf(f, "# Output for elevation_maps.c\n");
        fprintf(f, "%d %d\n", size_x, size_y);
        fprintf(f, "%d\n", 255);
        fwrite(image, size_x * size_y * sizeof(unsigned char), 1, f);
        fclose(f);
    }
}

void readPGMimage(const char *filename, unsigned char *image_array, int size_x, int size_y)
{
    // You DO NOT have to read or understand this function! it is
    // needed here to enable us to import a small image to work
    // with for the exercise.
    //
    // Reads the image stored in the specified file into the
    // specified image array. The image is assumed to be of size
    // (size_x x size_y) pixels. This should match the array size!

    FILE *f;
    char line[1024];
    int sizx, sizy;

    f = fopen(filename, "rb+");
    if (f == NULL)
    {
        fprintf(stderr, "Unable to open file %s for reading, please check name and path\n", filename);
        return;
    }
    fgets(&line[0], 1000, f);
    if (strcmp(&line[0], "P5\n") != 0)
    {
        fprintf(stderr, "Wrong file format, not a .pgm file or header end-of-line characters missing\n");
        fclose(f);
        return;
    }
    // Skip over comments
    fgets(&line[0], 511, f);
    while (line[0] == '#')
        fgets(&line[0], 511, f);
    sscanf(&line[0], "%d %d\n", &sizx, &sizy); // Read file size
    if (sizx != size_x || sizy != size_y)
    {
        fprintf(stderr, "Image has different size from what was specified in the function call!\n");
        fclose(f);
        return;
    }

    fgets(&line[0], 9, f); // Read the remaining header line

    fread(image_array, sizx * sizy * sizeof(unsigned char), 1, f);

    fclose(f);

    return;
}

void depth_first_search(unsigned char image_array[50][50], unsigned char levelset_map[50][50], int iy, int ix, unsigned char target)
{
    if (ix >= 50 || ix < 0 || iy >= 50 || iy < 0 || image_array[iy][ix] != target || levelset_map[iy][ix] != 0)
    {
        return;
    }

    levelset_map[iy][ix] = target;

    depth_first_search(image_array, levelset_map, iy + 1, ix, target);
    depth_first_search(image_array, levelset_map, iy - 1, ix, target);
    depth_first_search(image_array, levelset_map, iy, ix + 1, target);
    depth_first_search(image_array, levelset_map, iy, ix - 1, target);
}
// extract_levelset() is THE ONLY FUNCTION YOU NEED TO WORK ON.
void extract_levelset(unsigned char image_array[50][50], unsigned char levelset_map[50][50], int iy, int ix)
{
    unsigned char target = image_array[iy][ix];
    depth_first_search(image_array, levelset_map, iy, ix, target);
}

#ifndef __testing
int main()
{
    unsigned char image_array[50][50];  // We'll be working with 50x50 images
    unsigned char levelset_map[50][50]; // This will contain the extracted region

    // Clear the levelset_map[][] to all zeros (all black)
    for (int i = 0; i < 50; i++)
        for (int j = 0; j < 50; j++)
            levelset_map[i][j] = 0;

    // Read the selected input image into image_array[][]
    readPGMimage("Mars_elevation_crop1.pgm", &image_array[0][0], 50, 50);

    fprintf(stderr, "Extracting levelset!\n");
    extract_levelset(image_array, levelset_map, 5, 27);
    fprintf(stderr, "Done!\n");

    writePGMimage(&levelset_map[0][0], 50, 50);
    return 0;
}
#endif
