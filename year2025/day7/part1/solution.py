#!/usr/bin/env python3
# Day 7: Laboratories, Part 1

FILE_PATH = "../.input"

SOURCE = 'S'
TACHYON_BEAM = '|'
EMPTY_SPACE = '.'
SPLITTER = '^'

def print_manifold(manifold: list[list[int]]) -> None:
    print(f"\n{'\n'.join(''.join(i) for i in manifold)}")

def main():
    split_count = 0
    manifold = []

    with open(FILE_PATH, 'r') as manifold_file:
        for line in manifold_file:
            manifold.append(list(line.strip()))

    #print("DEBUG: starting manifold: ", end='')
    #print_manifold(manifold)

    for j in range(num_cols):
        if manifold[0][j] == SOURCE:
            manifold[0][j] = TACHYON_BEAM
            break

    for i, row in enumerate(manifold):
        #print(f"DEBUG: row {i:03}: {''.join(row)}")
        if i == len(manifold) - 1:
            break
        for j, char in enumerate(row):
            if char == TACHYON_BEAM:
                below = manifold[i+1][j]
                if below == EMPTY_SPACE:
                    manifold[i+1][j] = TACHYON_BEAM
                elif below == SPLITTER:
                    split_count += 1
                    if manifold[i+1][j-1] == EMPTY_SPACE:  # Left
                        manifold[i+1][j-1] = TACHYON_BEAM
                    if manifold[i+1][j+1] == EMPTY_SPACE:  # Right
                        manifold[i+1][j+1] = TACHYON_BEAM

    #print("DEBUG: ending manifold: ", end='')
    #print_manifold(manifold)

    print(f"Total splits: {split_count}")

if __name__ == "__main__":
    main()
