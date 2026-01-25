#!/usr/bin/env python3
# Day 9: Movie Theater, Part 2

FILE_PATH = "../.temp"

def area(t1: (int, int), t2: (int, int)) -> int:
    width = abs(t2[0] - t1[0]) + 1
    height = abs(t2[1] - t1[1]) + 1
    return width * height

def main():
    red_tiles = []

    with open(FILE_PATH, 'r') as red_tile_file:
        for line in red_tile_file:
            line.rstrip('\n')
            x, y = line.split(',')
            red_tiles.append((int(x), int(y)))

    max_area = 0
    num_tiles = len(red_tiles)

if __name__ == "__main__":
    main()
