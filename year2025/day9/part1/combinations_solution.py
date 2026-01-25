#!/usr/bin/env python3
# Day 9: Movie Theater, Part 1

from itertools import combinations

FILE_PATH = "../.input"

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

    # Runs basically the same, easier to read though
    for t1, t2 in combinations(red_tiles, 2):
        cur_area = area(t1, t2)
        #print(f"DEBUG: {t1[0]},{t1[1]} * {t2[0]},{t2[1]} = {cur_area}")
        max_area = max(max_area, cur_area)

    print(f"Largest area: {max_area}")

if __name__ == "__main__":
    main()
