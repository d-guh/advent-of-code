#!/usr/bin/env python3
# Day 5: Cafeteria, Part 1

FILE_PATH = "../.input"

def main():
    total_fresh = 0
    id_ranges = []
    ingredient_ids = []

    with open(FILE_PATH, 'r') as ids_file:
        range_flag = True  # Was debating using split here on every line and checking length of results, but this will probably translate better anyways? May also be more efficient
        for line in ids_file:
            line = line.strip()
            if line == '':
                range_flag = False
                continue
            if range_flag:
                id_ranges.append(tuple(map(int, line.split('-'))))
            else:
                ingredient_ids.append(int(line))  # Could technically make this in place rather that storing in memory

    for ingredient_id in ingredient_ids:
        for bot, top in id_ranges:
            # print(f"DEBUG: {bot}, {ingredient_id}, {top}")
            if bot <= ingredient_id <= top:
                total_fresh += 1
                break

    # print(f"DEBUG: {id_ranges}")
    # print(f"DEBUG: {ingredient_ids}")
    print(f"Total Fresh IDs: {total_fresh}")

if __name__ == "__main__":
    main()
