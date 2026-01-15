#!/usr/bin/env python3
# Day 5: Cafeteria, Part 2

FILE_PATH = "../.input"

def main():
    total_fresh = 0
    id_ranges = []
    merged_ranges = []

    with open(FILE_PATH, 'r') as ids_file:
        for line in ids_file:
            line = line.strip()
            if line == '':
                break
            id_ranges.append(list(map(int, line.split('-'))))
    
    id_ranges.sort(key=lambda x: x[0])
    # print(f"DEBUG: Orig Ranges: {id_ranges}")

    for cur_range in id_ranges:
        # Empty or non-overlap (add)
        if not merged_ranges or merged_ranges[-1][1] < cur_range[0]:
            merged_ranges.append(cur_range)
        # Overlap (merge)
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], cur_range[1])

    # print(f"DEBUG: Combined Ranges: {merged_ranges}")

    for start, end in merged_ranges:
        total_fresh += end - start + 1

    print(f"Total Fresh IDs: {total_fresh}")

if __name__ == "__main__":
    main()
