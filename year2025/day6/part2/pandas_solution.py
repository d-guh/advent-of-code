#!/usr/bin/env python3
# Day 6: Trash Compactor, Part 2: Pandas edition
import pandas as pd
import numpy as np

FILE_PATH = "../.input"

def main():
    total = 0
    worksheet = []

    with open(FILE_PATH, 'r') as worksheet_file:
        lines = worksheet_file.read().splitlines()

    df = pd.DataFrame(lines, columns=['line'])

    worksheet = df['line'].apply(lambda x: pd.Series(list(x))).T  # Transpose
    worksheet.replace(' ', np.nan, inplace=True)
    worksheet.dropna(axis=0, how='all', inplace=True)  # Drop empty cols

    #print(f"DEBUG:\n{worksheet}")

    numbers = []
    worksheet_collapsed = []

    for col in reversed(worksheet.values.tolist()):
        number = ''.join(char for char in col[:-1] if pd.notna(char))
        operator = col[-1].strip() if pd.notna(col[-1]) else ''
        if number:
            numbers.append(int(number))
        if operator:
            worksheet_collapsed.append((*numbers, operator))
            numbers.clear()

    worksheet = tuple(worksheet_collapsed)
    del worksheet_collapsed, numbers

    #print(f"DEBUG:\n{worksheet}")

    for equation in worksheet:
        operator = equation[-1]
        value = 0 if operator == '+' else 1

        for op in equation[:-1]:
            #print(f"DEBUG: op: {value} {operator} {op} = ", end='')
            if operator == '+':
                value += op
            else:
                value *= op
            #print(value)
        #print(f"DEBUG: tot: {total} + {value} = ", end='')
        total += value
        #print(total)
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
