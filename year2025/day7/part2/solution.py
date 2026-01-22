#!/usr/bin/env python3
# Day 7: Laboratories, Part 2

FILE_PATH = "../.input"

SOURCE = 'S'
TACHYON_BEAM = '|'
EMPTY_SPACE = '.'
SPLITTER = '^'

def print_manifold(manifold: list[list[int]]) -> None:
    print(f"\n{'\n'.join(''.join(i) for i in manifold)}")

def main():
    manifold = []

    with open(FILE_PATH, 'r') as manifold_file:
        for line in manifold_file:
            manifold.append(list(line.strip()))

    #print("DEBUG: starting manifold: ", end='')
    #print_manifold(manifold)

    num_rows = len(manifold)
    num_cols = len(manifold[0])

    counts = [[0] * num_cols for _ in range(num_rows)]

    for j in range(num_cols):
        if manifold[0][j] == SOURCE:
            counts[0][j] = 1
            break

    for r in range(num_rows - 1):
        #print(f"DEBUG: row {r:03}: {''.join(manifold[r])}  {str(counts[r])}")
        for c in range(num_cols):
            count = counts[r][c]
            if count == 0:
                continue

            below = manifold[r+1][c]

            if below == SPLITTER:
                counts[r+1][c-1] += count  # Left
                counts[r+1][c+1] += count  # Right
            else:
                counts[r+1][c] += count  # Bring down

    total_timelines = sum(counts[num_rows - 1])
    print(f"Total timelines: {total_timelines}")

if __name__ == "__main__":
    main()
