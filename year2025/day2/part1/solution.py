#!/usr/bin/env python3
# Day 2: Gift Shop, Part 1

import csv

FILE_PATH = "../.input"

def main():
    # invalid_ids = []  # Useful for debugging but not needed to store them all
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

                half_length = length // 2  # Assumes even length IDs (since pattern double)
                first_half = id_str[:half_length]
                second_half = id_str[half_length:]

                if first_half == second_half:
                    # invalid_ids.append(cur_id)  # Debug
                    invalid_total += cur_id
    
    # print(invalid_ids)  # Debug
    # print(sum(invalid_ids))  # Debug/Answer
    print(invalid_total)

if __name__ == "__main__":
    main()
