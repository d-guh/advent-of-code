#!/usr/bin/env python3
# Day 2: Gift Shop, Part 1

import csv

FILE_PATH = "../.input"

def main():
    invalid_total = 0

    with open(FILE_PATH, 'r') as ids_file:
        idreader = csv.reader(ids_file)
        id_ranges = next(idreader)
        # print(f"DEBUG: all ranges: {id_ranges}")
        for id_range in id_ranges:
            id_range_split = id_range.split('-')
            # print(f"DEBUG: each range: {id_range_split}")
            start_id = id_range_split[0]
            end_id = id_range_split[1]
            for cur_id in range(int(start_id), int(end_id)+1):
                id_str = str(cur_id)
                length = len(id_str)

                if length % 1 == 0:  # Only check ids that are even
                    half_length = length // 2
                    first_half = id_str[:half_length]
                    second_half = id_str[half_length:]

                    if first_half == second_half:
                        # print(f"DEBUG: MATCH: {cur_id}")
                        invalid_total += cur_id

    print(invalid_total)

if __name__ == "__main__":
    main()
