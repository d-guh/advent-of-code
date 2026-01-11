#!/usr/bin/env python3
# Day 3: Lobby, Part 2
# DO NOT USE THIS ONE LMAO
# This one is incredibly slow, combinations is super inefficient to be used in this way.

from itertools import combinations

FILE_PATH = "../.input"

def main():
    total_joltage = 0
    num_batteries = 12

    with open(FILE_PATH, 'r') as banks_file:
        for bank in banks_file:
            bank = bank.strip()
            combined_joltage = "".join(max(combinations(bank, num_batteries)))
            # print(f"DEBUG: {bank}: {combined_joltage}")
            total_joltage += int(combined_joltage)

    print(f"Total Joltage: {total_joltage}")

if __name__ == "__main__":
    main()
