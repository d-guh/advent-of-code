#!/usr/bin/env python3
# Day 2: Gift Shop, Part 2

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

                for i in range(1, length // 2 + 1):  # Only need to check half length
                    if length % i == 0:  # Only check if divisible by pattern length
                        pattern = id_str[:i]
                        if pattern * (length // i) == id_str:  # repeat pattern as many times as possible
                            # print(f"DEBUG: MATCH: {cur_id}")
                            invalid_total += cur_id
                            break

    print(invalid_total)

if __name__ == "__main__":
    main()
