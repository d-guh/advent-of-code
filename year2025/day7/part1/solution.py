#!/usr/bin/env python3
# Day 7: Laboratories, Part 1

FILE_PATH = "../.input"

SOURCE = 'S'
TACHYON_BEAM = '|'
EMPTY_SPACE = '.'
SPLITTER = '^'

def main():
    split_count = 0
    manifold = []

    with open(FILE_PATH, 'r') as manifold_file:
        for line in manifold_file:
            manifold.append(list(line.strip()))

    #print(f"DEBUG: starting manifold:\n{'\n'.join(''.join(i) for i in manifold)}")

    manifold[0] = [TACHYON_BEAM if c == SOURCE else c for c in manifold[0]]
    for i, row in enumerate(manifold):
        #print(f"DEBUG: row {i:03}: {''.join(row)}")
        if i == len(manifold) - 1:
            break
        for j, char in enumerate(row):
            if char == TACHYON_BEAM:
                if manifold[i+1][j] == EMPTY_SPACE:
                    manifold[i+1][j] = TACHYON_BEAM
                elif manifold[i+1][j] == SPLITTER:
                    split_count += 1
                    if manifold[i+1][j-1] == EMPTY_SPACE:  # Left
                        manifold[i+1][j-1] = TACHYON_BEAM
                    if manifold[i+1][j+1] == EMPTY_SPACE:  # Right
                        manifold[i+1][j+1] = TACHYON_BEAM

    #print(f"DEBUG: ending manifold:\n{'\n'.join(''.join(i) for i in manifold)}")

    print(f"Total splits: {split_count}")

if __name__ == "__main__":
    main()
