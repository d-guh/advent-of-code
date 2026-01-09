#!/usr/bin/env python3
# Day 3: Lobby, Part 1
# Yeah this is kinda bummy but use the resources at hand I suppose, good for verifying other solutions.

from itertools import combinations

FILE_PATH = "../.input"

def main():
    total_joltage = 0

    with open(FILE_PATH, 'r') as banks_file:
        for bank in banks_file:
            bank = bank.strip()
            combined_joltage = "".join(max(combinations(bank, 2)))
            # print(f"DEBUG: {bank}: {combined_joltage}")
            total_joltage += int(combined_joltage)

    print(f"Total Joltage: {total_joltage}")

if __name__ == "__main__":
    main()
