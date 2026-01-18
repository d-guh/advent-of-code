#!/usr/bin/env python3
# Day 6: Trash Compactor, Part 1

FILE_PATH = "../.input"

def main():
    total = 0
    worksheet = []

    with open(FILE_PATH, 'r') as worksheet_file:
        worksheet = [line.split() for line in worksheet_file]
    
    worksheet = [tuple(row) for row in zip(*worksheet)]

    #print(f"DEBUG:\n{worksheet}")

    for equation in worksheet:
        operator = equation[-1]
        value = 0 if operator == '+' else 1

        for op in equation[:-1]:
            #print(f"DEBUG: op: {value} {operator} {op} = ", end='')
            if operator == '+':
                value += int(op)
            else:
                value *= int(op)
            #print(value)
        #print(f"DEBUG: tot: {total} + {value} = ", end='')
        total += value
        #print(total)

    print(f"Total: {total}")

if __name__ == "__main__":
    main()
