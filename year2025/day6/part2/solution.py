#!/usr/bin/env python3
# Day 6: Trash Compactor, Part 2

FILE_PATH = "../.input"

def main():
    total = 0
    worksheet = []

    with open(FILE_PATH, 'r') as worksheet_file:
        worksheet = [line.rstrip('\n') for line in worksheet_file]

    worksheet = list(zip(*worksheet))
    worksheet = [col for col in worksheet if any(char != ' ' for char in col)]  # Remove empty columns

    numbers = []
    worksheet_collapsed = []
    for col in reversed(worksheet):
        number = ''.join(char for char in col[:-1] if char != ' ')
        operator = col[-1].strip()
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
