#!/usr/bin/env python3
# Day 6: Trash Compactor, Part 1; Pandas edition

import pandas as pd

FILE_PATH = "../.input"

def main():
    total = 0

    df = pd.read_csv(FILE_PATH, header=None, sep="\\s+")
    worksheet = df.transpose()

    # print(f"DEBUG:\n{worksheet}")

    for equation in worksheet.values:
        operator = equation[-1]
        value = 0 if operator == '+' else 1

        for op in equation[:-1]:
            if operator == '+':
                value += int(op)
            else:
                value *= int(op)

        total += value

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
